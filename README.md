# WebCrawling_python
BeautifulSoup를 활용해 네이버 블로그 탭의 검색결과를 크롤링하는 과정이다. 유튜브 채널 [프로그래머 김플 스튜디오](https://www.youtube.com/channel/UCdNSo3yB5-FRTFGbUNKNnwQ)님의 파이썬 Beautifulsoup 크롤링 예제를 보며 만들었다.

```python
import urllib.request # html을 읽어오기 위한 모듈
import urllib.parse  # 한글입력(plusUrl)이 들어와도 변환시켜줌
from bs4 import BeautifulSoup
```
사용된 모듈이며 코드는 완성본인 Crawlier_beautifulsoup_2.py 기준이다. 최초 코드는 '파이썬'만을 검색만 결과를 보여주는데 제한되었지만, 검색어부분을 plusUrl 이란 변수에 할당해 줌으로써 보다 다양한 검색을 끌어올 수 있도록 했다.   

```python
url = baseUrl + urllib.parse.quote_plus(plusUrl)  # 한글이 오면 전환시켜줌
```
파서를 활용해 한글입력이 들어왔을 때에도 오류없이 정상적인 url로 변환시켜준다
