# web2.py
#웹서버에 요청
import urllib.request
#크롤링
from bs4 import BeautifulSoup

data = urllib.request.urlopen("http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")
soup = BeautifulSoup(data, "html.parser")

# ctrl + / :다중 라인 주석 
# <td class="title">
# 	<a href="/webtoon/detail?titleId=20853">마음의 소리 50화 <격렬한 나의 하루> </a>
# </td>


                        