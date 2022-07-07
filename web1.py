# web1.py 
#웹크롤링(웹 데이터 수집 기술)
from bs4 import BeautifulSoup

#문서 로딩 
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()
#검색이 용이한 객체 
soup = BeautifulSoup(page, "html.parser")
print(soup.prettify())

