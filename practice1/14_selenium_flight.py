from selenium import webdriver
from selenium.webdriver.common.by import By   # 로딩페이지 기다릴때 밑에 2줄과 함께 추가
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window() #창최대화

url = "https://beta-m-flight.naver.com/"

browser.get(url)

browser.find_element_by_link_text("가는 날)").click()

# 이번달 27일 28일 선택
browser.find_element_by_link_text("27")[0].click() 
browser.find_element_by_link_text("28")[0].click() 

browser.find_element_by_xpath("제주도선택").click()

browser.find_element_by_link_text("항공권 검색").click()

try:
    elem = WebDriverWait(browser, 10).until(EC.presece_of_element_located((By.XPATH, "검색결과")))
    #성공시 수행
finally:
    browser.quit()

#첫번째 결과 출력

# elem = browser.find_element_by_xpath("검색결과")
# print(elem.text)