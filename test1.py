from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import parse
import re
from openpyxl import load_workbook

import pandas as pd

xlsx = pd.read_excel("book1.xlsx")
xlsx.to_csv("book1.csv")
# row 생략 없이 출력
pd.set_option('display.max_rows', None)
# col 생략 없이 출력
pd.set_option('display.max_columns', None)
a=xlsx[['Unnamed: 3','Unnamed: 5','Unnamed: 8']].loc[2:len(xlsx)]
a=a.dropna(axis=0)
ac=a.values.tolist()
# url은 ASCII 문자열을 이용해서만 전송될 수 있다. 즉 ASCII가 아닌 한글,
# 특수 문자(Unsafe, Reserved)는 두개의 16진수를 사용하는 octet형태로 encode된다.
ac=[]
ac=a.values.tolist()
err=[["틀린거","틀린거","틀린거","틀린거","틀린거"]]



for i in range(len(ac)):
  url = "https://search.kyobobook.co.kr/web/search?vPstrKeyWord="
  book_name =ac[i][0] +" " +ac[i][1]
  book_name=parse.quote(book_name)
  url= url + book_name

  html = urlopen(url)
  bsObject = BeautifulSoup(html, "html.parser")

  try:
    author = bsObject.select("td.detail div.author")
    pauthor = (author[0].text).replace("\t","").replace("\r","").replace("\n","")
    titles = bsObject.select("td.detail div.title strong")
    price = bsObject.select("td.price div.org_price del")

  except:
    try:
      url = "https://search.kyobobook.co.kr/web/search?vPstrKeyWord="
      book_name =ac[i][0]
      book_name=parse.quote(book_name)
      url= url + book_name
      html = urlopen(url)
      bsObject = BeautifulSoup(html, "html.parser")

      author = bsObject.select("td.detail div.author")
      pauthor = (author[0].text).replace("\t","").replace("\r","").replace("\n","")
      titles = bsObject.select("td.detail div.title strong")
      ac[i].append("출판사이름 정확x")
  # print(titles[0].text)
      price = bsObject.select("td.price div.org_price del")
    except:
      ac[i].append("NAN")

      continue
# print(price[0].text)
  ac[i].append(int(price[0].text.replace(",","")))
  # ac[i].append(pauthor)
  if ac[i][2]!=ac[i][3]:
    err.append(ac[i])
  print(ac[i])

print(ac)

