import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액 1-200.csv"
f = open(filename, "w", encoding="utf8", newline="")  # 뉴라인안쓰면 한칸자동띄움  #한글깨질때는 utf-8-sig 로 바꿔서 트라이
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t")
#["N", "종목명", "현재가", ...] 이런식으로 리스트형태로 들어감 "복붙".스플릿  =>편법인듯
print(type(title))

writer.writerow(title)

for page in range(1, 5):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1: 
            continue
        data = [column.get_text().strip() for column in columns]
        # print(data)
        writer.writerow(data)
