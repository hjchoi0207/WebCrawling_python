# https://www.youtube.com/watch?v=hKApZHK_fOQ
# beautifulsoup를 이용한다.
import urllib.request
from bs4 import BeautifulSoup

# 네이버에 파이썬 검색 후 블로그탭 url
url = "https://search.naver.com/search.naver?where=post&sm=tab_jum&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC"
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
