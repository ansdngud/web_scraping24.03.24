import requests
from bs4 import BeautifulSoup

# 웹페이지 URL 설정
url = 'https://www.naver.com/'

# GET 요청 보내기
resp = requests.get(url)

html = """
<nav class="menu-box-1" id="menu-box">
  <ul>
    <li>
      <a href="https://www.naver.com">네이버로 이동</a>
    </li>
    <li>
      <a href="https://www.google.com">구글로 이동</a>
    </li>
    <li>
      <a href="https://www.daum.net">다음으로 이동</a>
    </li>
  </ul>
</nav>
"""

# HTML 파싱
bs = BeautifulSoup(html, 'html.parser')

# 첫번째로 이치하는 단일 요소의 접근
a_tag = bs.select_one('a')

# 모든 일치하는 요소로 접근할 때 사용, 리스트 반환
a_tags = bs.select('a')

# get_text() : 해당 엘리먼트가 품고 있는 텍스트 출력
for tags in a_tags:
  print(tags.get_text())
  
# get('href') : 해당 엘리먼트가 가지고 있는 속성 값을 출력
for tags in a_tags:
  print(tags.get('href'))