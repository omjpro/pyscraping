from selenium import webdriver
import time

browser = webdriver.Chrome("./chromedriver.exe")
browser.maximize_window() #창최대화

url = "https://section.cafe.naver.com/ca-fe/home/search/cafes?q=%EC%A3%BC%EC%A3%BC&th=20"
browser.get(url)

interval = 2 

browser.find_element_by_link_text("헬릭스미스").click()
