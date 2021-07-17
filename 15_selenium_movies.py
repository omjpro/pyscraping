import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language":"ko-KR,ko"
}  #억셉트 부분은 한글페이지 있는 경우 한글로달라는 추가 구문 

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
print(len(movies))

with open("movie.html", "w", encoding="utf8") as f:
    # f.write(res.text)
    f.write(soup.prettify()) #html 문서를 예쁘게

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)

