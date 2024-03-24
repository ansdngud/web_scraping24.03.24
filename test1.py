import requests
from bs4 import BeautifulSoup

# 웹페이지 URL 설정
url = 'https://www.naver.com/'

# GET 요청 보내기
resp = requests.get(url)

# 네이버 뉴스 url
url = 'https://news.naver.com/section/103'

# resp : response의 약자
# requests를 이용해서 웹 페이지의 hrml 문서 내용 가져오기
# 지정 웹 사이트의 get요청을 보내서 
resp = requests.get(url)

# HTML 파싱 , 웹 페이지의 html 내용을 beatifulSoup 객체로 변환
bs = BeautifulSoup(resp.text, 'html.parser')

new_title = bs.find_all('a', class_='sa_text_title')

new_title_list = []

for title in new_title:
  new_title_list.append(title.get_text())
  
# 뉴스 제목안에 있던 \n을 제거하는 코드 
cleaned_news_tit = [item.replace('\n', '') for item in new_title_list]

for idx, tit in enumerate(cleaned_news_tit):
  print(f"{idx + 1} : {tit}")
  
keyword = '비'
keyword_tit_list = []
for tit in cleaned_news_tit:
  if keyword in tit:
    keyword_tit_list.append(tit)
    
print(keyword_tit_list)