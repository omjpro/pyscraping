from selenium import webdriver

from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome('C:\chromedriver', options=options)
driver.get('https://section.cafe.naver.com/ca-fe/home/search/cafes?q=%EC%A3%BC%EC%A3%BC&p=1&od=2&th=20')
html = driver.page_source #페이지의 소스코드
soup = BeautifulSoup(html, 'html.parser')


data_src = soup.find("p", id="cafe_introduction")

name = data_src.text

print(name)