import requests
from bs4 import BeautifulSoup

# HTML을 가져올 웹사이트의 URL
url = 'https://www.naver.com'

# HTTP GET 요청을 보내고 응답을 받음
resp = requests.get(url)

# 응답의 HTML을 BeautifulSoup을 사용하여 파싱
bs = BeautifulSoup(resp.text, 'html.parser')

# 응답의 HTML 내용 출력
print(bs)