import requests
import re
from bs4 import BeautifulSoup

url = "https://section.cafe.naver.com/ca-fe/home/search/cafes?q=%EC%A3%BC%EC%A3%BC&od=2&th=20"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("div", attrs={"class":"detail_area"})
print(items[0].find("span").get_text())

