# web2.py
#웹서버에 요청
import urllib.request
#크롤링
from bs4 import BeautifulSoup

#수열을 생성해서 URL주소 만들기
for i in range(1,6):
    url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page="

    data = urllib.request.urlopen("http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")
    soup = BeautifulSoup(data, "html.parser")
    # ctrl + / :다중 라인 주석 
    # <td class="title">
    # 	<a href="/webtoon/detail?titleId=20853">마음의 소리 50화 <격렬한 나의 하루> </a>
    # </td>
    cartoons = soup.find_all("td", class_="title")
    print("갯수:{0}".format(len(cartoons)))
    title = cartoons[0].find("a").text 
    link = cartoons[0].find("a")["href"]
    print(title)
    print(link)

    for item in cartoons:
        title = item.find("a").text
        print(title.strip())

                        