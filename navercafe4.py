from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}


url = "https://section.cafe.naver.com/ca-fe/home/search/cafes?q=%EC%A3%BC%EC%A3%BC&p=1&od=2&th=20"
browser.get(url, headers=headers)

# cafe = browser.find_element_by_xpath("//*[@id='app']/div/div[2]/div/div[1]/div[3]/div/div[3]/ul/li[1]/div/div/div/a/span")
# print(cafe.text)

with open("prac1.html", "w", encoding="utf8") as f:
    f.write(browser.text)
    
