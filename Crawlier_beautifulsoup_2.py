# https://www.youtube.com/watch?v=hKApZHK_fOQ
# beautifulsoup를 이용한다.
import urllib.request
import urllib.parse  # 한글입력(plusUrl)이 들어와도 변환시켜줌
from bs4 import BeautifulSoup

# 검색어를 바꿔가면서 기본 url을 확보, 이후 검색어 url과 결합하여 유동적인 크롤링
baseUrl = "https://search.naver.com/search.naver?where=post&sm=tab_jum&query="
plusUrl = input('검색어를 입력하세요 : ')
url = baseUrl + urllib.parse.quote_plus(plusUrl)  # 한글이 오면 전환시켜줌

html = urllib.request.urlopen(url).read()  # html을 가져온다
soup = BeautifulSoup(html, 'html.parser')  # Beautifulsoup로 분석

# print(soup) 모든 html을 가져옴

# find만 사용 시 결과 값은 하나
# sh_blog_title을 가진 class를 모두 찾아라
# 우리가 필요한 것은 href태그와 title 태그의 내용
title = soup.find_all(class_='sh_blog_title')
print(len(title))  # 결과는 10 : 네이버 블로그 페이지당 10개 씩 나오기 때문

for i in title:
    print(i.attrs['title'])
    print(i.attrs['href'])
    print()
