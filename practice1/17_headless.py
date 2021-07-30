
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

#유져에이전트 받아오기 
url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)
browser.quit()

# match() 처음부터 일치하는지
# search() 일치하는게 있는지
# findall() 일치하는 것 모든것을 리스트로반환
# requests 웹페이지 읽어오기 (동적X)  res.raise_for_status() 로 문제없는지 확인 
# selenium 동적O 느림, 크롬드라이버필요  => 이를 beuatifulsoup으로 데이터추출(스크래핑)
# 셀레늄 = find_element_by_id, class_name, link_text, by_xpath 로찾기
# 기다려야할때 