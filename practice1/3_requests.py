import requests
res = requests.get("http://naver.com")
#res = requests.get("http://nadocoding.tistory.com")
res.raise_for_status()   #오류시 바로 끝내기 구문
#print("응답코드 :", res.status_code) # 200이면 정상

# if res.status_code == requests.codes.ok:
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")


print(len(res.text))
print(res.text)

with open("mynaver.html", "w", encoding="utf8") as f:
    f.write(res.text)
    