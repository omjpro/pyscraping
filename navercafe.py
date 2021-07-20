import requests
import re
import csv
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

filename = "주주카페 리스트.csv"
f = open(filename, "w", encoding="utf8", newline="")  # 뉴라인안쓰면 한칸자동띄움  #한글깨질때는 utf-8-sig 로 바꿔서 트라이
writer = csv.writer(f)

for i in range(1, 4):
    url = "https://section.cafe.naver.com/ca-fe/home/search/cafes?q=%EC%A3%BC%EC%A3%BC&p={}&od=2&th=20".format(i)
    res = requests.get(url,headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    cafes = soup.find("a", attrs={"class":"cafe_name"}).find("span")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1: 
            continue
        data = [column.get_text().strip() for column in columns]
        # print(data)
        writer.writerow(data)


print


#     for cafe in cafes:
#         name = cafe.find("span").get_text() # 카페명
#         price = cafe.find("strong", attrs={"class":"price-value"}).get_text() 

#         # 리뷰 100개이상 평점 4.5이상 
#         rate = cafe.find("em", attrs={"class":"rating"}) # 평점
#         if rate:
#             rate = rate.get_text()
#         else:
#             # print(" <평점 없는 상품 제외합니다")
#             continue

#         rate_cnt = cafe.find("span", attrs={"class":"rating-total-count"}) #평가
        
#         if rate_cnt:
#             rate_cnt = rate_cnt.get_text()[1:-1]
#         else:
#             # print(" < 평점 수 없는 상품 제외>")
#             continue

#         link = cafe.find("a", attrs={"class":"search-product-link"})["href"]

#         if float(rate) >= 4.5 and int(rate_cnt) >= 100:
#             # print(name, price, rate, rate_cnt)
#             print(f"제품명 : {name}")
#             print(f"가격 : {price}")
#             print(f"평점 : {rate}점 ){rate_cnt}개)")
#             print("바로가기 : {}".format("https://www.coupang.com" + link))
#             print("-"*100)  #줄긋기



# f = open(filename, "w", encoding="utf8", newline="")
