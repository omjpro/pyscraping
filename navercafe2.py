import requests
from bs4 import BeautifulSoup

url = "https://section.cafe.naver.com/ca-fe/home/search/cafes?q=%EC%A3%BC%EC%A3%BC&p=1&od=2&th=20"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)
    


# cafes = soup.find("ul", attrs={"class":"CafeList"}).find("p", attrs={"class":"cafe_introduction"})
# print(cafes)
