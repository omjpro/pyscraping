
from selenium import webdriver

browser = webdriver.Chrome("./chromedriver.exe")


browser.maximize_window()

#페이지 이동 

url = "https://play.google.com/store/movies/top"
browser.get(url)

#스크롤내리기 자바스크립트 명령어
# browser.execute_script("window.scrollTo(0,1080)") # 1920 *1080모니터해상도에 따라 스크롤내리기
# browser.execute_script("window.scrollTo(0,2080)") # 지정한위치로 스크롤내리기

# browser.execute_script("window.scrollTo(0, document.body.scrollheught)")


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



import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs={"class": "Vpfmgd"})
print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)

