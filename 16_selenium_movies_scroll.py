# import requests
# from bs4 import BeautifulSoup

# url = "https://play.google.com/store/movies/top"

# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
#     "Accept-Language":"ko-KR,ko"
# }  #억셉트 부분은 한글페이지 있는 경우 한글로달라는 추가 구문 

# res = requests.get(url, headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")

# movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
# print(len(movies))

# with open("movie.html", "w", encoding="utf8") as f:
#     # f.write(res.text)
#     f.write(soup.prettify()) #html 문서를 예쁘게

# for movie in movies:
#     title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
#     print(title)

from selenium import Webdriver
browser - webdriver.chome()
browser.maximize_window()

#페이지 이동 

url = "https://play.google.com/store/movies/top"
browser.get(url)

#스크롤내리기 자바스크립트 명령어
# browser.execute_script("window.scrollTo(0,1080)") # 1920 *1080모니터해상도에 따라 스크롤내리기
# browser.execute_script("window.scrollTo(0,2080)") # 지정한위치로 스크롤내리기

browser.execute_script("window.scrollTo(0, document.body.scrollheught)")


import time

interval = 2 

prev_height = browser.execute_script("return document.body.scrollHeight")

#반복수행

while True:

    browser.execute_script("return document.body.scrollHeight")

    time.sleep(interval)

    curr_height = browser.execute_script("return document.body.scrollHeight")

    if curr_height == prev_height:
        break
    

    prev_height = curr_height

print("스크롤완료")




