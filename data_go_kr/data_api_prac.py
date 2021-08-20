import requests, xmltodict, json

key = 'e72fbd752d504b0da5b532f57274ac19	'

pIndex = 1                  #Integer 페이지 위치
pSize = 50                   #Integer 페이지 당 요청수
SIGUN_NM = "가평군"               #String 시군명
SIGUN_CD = "41820"               #String 시군코드


url = "https://openapi.gg.go.kr/Resrestrtcvnstr?KEY={0}&pindex={1}&pSize={2}&&SIGUN_CD={3}".format(key, pIndex, pSize, SIGUN_CD)

content = requests.get(url).content
dict = xmltodict.parse(content)
jsonString = json.dumps(dict['Resrestrtcvnstr'], ensure_ascii=False)
print(jsonString)
