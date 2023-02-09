# Bookprice_check
[파이썬] 책 구입목록(excel)를 받아 영풍문구 스크래핑하여 책 가격이 제대로 입력됬는지 체킹하는 실행파일  
## 프로젝트 계획 이유 
공익 복무 중인 도서관에서 한달에 두세번씩 책 구입 목록을 받아 영풍문구에서 책 가격이 정확하게 적혀있는지 확인하는 업무가 있음. 한번에 100개 정도를 구매하는데 일일이 책 이름과 저자를 검색해서 가격을 확인하는게 귀찮아 이를 자동으로 해주는 실행 파일을 만듬.
## 설명 
도서관에서 책 구입할 목록이 담긴 아래같은 xlsx파일을 받습니다.
![EX1](https://user-images.githubusercontent.com/28581494/140741659-1f9a4b61-5185-4c99-be28-ed739e7f4e75.PNG)  
이를 dataFrame으로 변환하여 도서이름, 출판사, 책 가격을 가져온 뒤 
BeautifulSoup를 이용해 영풍문구에서 스크래핑해온  책 가격과 비교하여 책 가격이 이상한걸 체킹 
pyqt5를 이용해 pyqt5로 ui를 만들고 pyinstaller로 실행 파일을 만듬 

![Ex2](https://user-images.githubusercontent.com/28581494/140743254-72250ae8-87e7-4bbf-b631-10d3a99b683f.PNG)
기존 가격과 다른 경우 - 4번째 행에 NAN 표시하고 5행에 다른 가격 출력  , 6행에 xxxxx 출력
출판사 이름이 잘못된 경우 - 5번째 행에 "출판사 이름 정확x" 출력 , 6행에 xxxxx 출력 

## 실행 파일 생성 방법 
pip으로 pyinstaller 설치  
  pip install pyinstaller
  
실행 파일 생성 (콜솔창 없이, 실행파일 하나만 생성) 
  pyinstaller bookprice.py -w -F
끝 - dist 폴더안에 실행파일 생김 

## 배운점 
BeautifulSoup을 이용해 스크래핑 해오는 방법을 익힐 수 있었음
pyqt5를 이용해 간단한 gui를 만들어봄 
pyinstaller로 실행파일(exe)를 만드는 방법을 익힘 

