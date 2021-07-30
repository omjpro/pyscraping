from libs.driverGetter import getDriver
import time

url = "https://www.naver.com/"
url = "https://nid.naver.com/nidlogin.login?mode=form&url"


driver = webdriver.Chrome("./chromedriver.exe")
driver.maximize_window() #창최대화

driver.get(url)

driver.find_element_by_xpath().send_keys()
driver.find_element_by_xpath().send_keys()
driver.find_element_by_xpath().send_keys()

time.sleep(20)

url = "https://cafe.naver.com"

driver.get(url)

keyword = "주주"

pageString = driver.page_source
print = 