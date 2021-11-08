from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import parse
import pandas as pd
import sys
from PyQt5.QtWidgets import *
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("책가격 check")
        self.setGeometry(100, 100, 1100, 800)
        self.pushButton1= QPushButton("파일찾기")
        self.layout = QVBoxLayout()
        self.pushButton1.clicked.connect(self.pushButtonClicked)
        self.tablewidget = QTableWidget(self)
        self.tablewidget.resize(1100, 400)
        self.tablewidget.setRowCount(150)  # 행 개수
        self.tablewidget.setColumnCount(6)  # 열 개수
        self.tablewidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.label = QLabel()
        self.layout.addWidget(self.pushButton1)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.tablewidget)
        self.setLayout(self.layout)
    def pushButtonClicked(self):
        global ac
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')
        print(fname[0])
        xlsx = pd.read_excel(""+fname[0], sheet_name="선정목록")
        print(xlsx)
        xlsx.to_csv("book1.csv")
        # row 생략 없이 출력
        pd.set_option('display.max_rows', None)
        # col 생략 없이 출력
        pd.set_option('display.max_columns', None)
        a = xlsx[['Unnamed: 3', 'Unnamed: 5', 'Unnamed: 8']].loc[2:len(xlsx)-2]
        print(a)
        a = a.dropna(axis=0)
        ac = a.values.tolist()
        for i in range(len(ac)):
            url = "https://search.kyobobook.co.kr/web/search?vPstrKeyWord="
            book_name = ac[i][0] + " " + ac[i][1]
            book_name = parse.quote(book_name)
            url = url + book_name
            html = urlopen(url)
            bsObject = BeautifulSoup(html, "html.parser")
            try:
                author = bsObject.select("td.detail div.author")
                print(author)
                pauthor = (author[0].text).replace("\t", "").replace("\r", "").replace("\n", "")
                titles = bsObject.select("td.detail div.title strong")
                price = bsObject.select("td.price div.org_price del")
            except:
                try:
                    url = "https://search.kyobobook.co.kr/web/search?vPstrKeyWord="
                    book_name = ac[i][0]
                    book_name = parse.quote(book_name)
                    url = url + book_name
                    html = urlopen(url)
                    bsObject = BeautifulSoup(html, "html.parser")
                    author = bsObject.select("td.detail div.author")
                    pauthor = (author[0].text).replace("\t", "").replace("\r", "").replace("\n", "")
                    titles = bsObject.select("td.detail div.title strong")
                    ac[i].append("출판사이름 정확x")
                    # print(titles[0].text)
                    price = bsObject.select("td.price div.org_price del")
                except:
                    ac[i].append("NAN")
            # print(price[0].text)
            ac[i].append(int(price[0].text.replace(",", "")))
            # ac[i].append(pauthor)
            if ac[i][2] != ac[i][3]:
                ac[i].append("xxxxx")
        self.label.setText(ac[0][0])
        for i in range(len(ac)):
            for j in  range(len(ac[i])):
                try:
                    self.tablewidget.setItem(i, j, QTableWidgetItem(str(ac[i][j])))
                except:
                    continue
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()