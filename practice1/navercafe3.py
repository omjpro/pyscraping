from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://section.cafe.naver.com/ca-fe/home/search/cafes?q=%EC%A3%BC%EC%A3%BC&p=1&od=2&th=20")

names = browser.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div[3]/div/div[3]/ul/li[1]/div/div/div/a/span")

print(names)

browser.quit()