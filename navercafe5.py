from selenium import webdriver
from selenium.webdriver.common.by import By   # 로딩페이지 기다릴때 밑에 2줄과 함께 추가
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window() #창최대화

url = "https://section.cafe.naver.com/ca-fe/home/search/cafes?q=%EC%A3%BC%EC%A3%BC&p=1&od=2&th=20"
browser.get(url)

browser.find_element_by_xpath("헬릭스미스").click()
