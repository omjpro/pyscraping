
# 모듈 추가
import requests
from urllib.parse import urlparse
import pandas as pd

lon = 127.947727443701; lat = 37.337061376149 # 국립공원연구원 위치
page=1 # 첫번째 페이지
url = "https://dapi.kakao.com/v2/local/search/category.json?&category_group_code=CS2&x="\
+str(lon)+"&y="+str(lat)+"&page="+str(page)+"&radius=1000" # 카카오맵 API
json_obj = requests.get(urlparse(url).geturl(),headers={"Authorization":"KakaoAK 4d25f7ae6c4cab6bc96c746280e403af"}).json()

# 첫번째 편의점 정보
json_obj['documents'][0]

# 첫번째 편의점 정보 데이터프레임
pd.DataFrame(json_obj['documents'][0], index=[0])[['place_name','road_address_name', 'distance', 'x', 'y']]

# 반복문을 위한 데이터프레임 구성
df = pd.DataFrame(columns = ['place_name','road_address_name', 'distance', 'x', 'y'])
df_s = pd.DataFrame(json_obj['documents'][0], index=[0])[['place_name','road_address_name', 'distance', 'x', 'y']]
df = df.append(df_s)
df.head()

# 메타정보
json_obj['meta']



# 메타정보 조건문 정의
if json_obj['meta']['is_end'] == False:
    print("False")
else:
    print("True")


# 편의점 검색 함수 정의
def search_CVS(lon, lat):
    df = pd.DataFrame(columns = ['place_name','road_address_name', 'distance', 'x', 'y'])
    page = 1
    while True:
        url = "https://dapi.kakao.com/v2/local/search/category.json?&category_group_code=CS2&x="\
        +str(lon)+"&y="+str(lat)+"&page="+str(page)+"&radius=1000"
        json_obj = requests.get(urlparse(url).geturl(),headers={"Authorization":"KakaoAK 4d25f7ae6c4cab6bc96c746280e403af"}).json()
        for document in json_obj['documents']:
            df_s = pd.DataFrame(document, index=[0])[['place_name','road_address_name', 'distance', 'x', 'y']]
            df = df.append(df_s)
        if json_obj['meta']['is_end'] == False:
            page += 1
        else:
            return df

# 편의점 검색 함수 테스트
df = search_CVS(127.947727443701, 37.337061376149)

# 편의점 정보
df.head()


# 가장 가까운 편의점 확인
df.sort_values(by=['distance'], ascending=True).head()


# 편의점 개수
len(df)

# 경도
df.iloc[0, 3]

# QGIS 파이썬콘솔: 국립공원연구원 임시 레이어 추가
'''
vl = QgsVectorLayer("Point?crs=EPSG:4326", "국립공원연구원", "memory")
pr = vl.dataProvider()
pr.addAttributes([QgsField("place_name", QVariant.String),
                  QgsField("lon", QVariant.Double),
                  QgsField("lat", QVariant.Double)])
vl.updateFields()
for i in range(len(df)):
    f = QgsFeature()
    f.setGeometry(QgsGeometry.fromPointXY(127.947727443701, 37.337061376149)))
    f.setAttributes(['국립공원연구원', 127.947727443701, 37.337061376149])
    pr.addFeature(f)
vl.updateExtents()
QgsProject.instance().addMapLayer(vl)
'''

# QGIS 파이썬콘솔: 편의점 검색 함수 정의
def search_CVS(lon, lat):
    df = pd.DataFrame(columns = ['place_name','road_address_name', 'distance', 'x', 'y'])
    page = 1
    while True:
        url = "https://dapi.kakao.com/v2/local/search/category.json?&category_group_code=CS2&x="\
        +str(lon)+"&y="+str(lat)+"&page="+str(page)+"&radius=1000"
        json_obj = requests.get(urlparse(url).geturl(),headers={"Authorization":"KakaoAK 4d25f7ae6c4cab6bc96c746280e403af"}).json()
        for document in json_obj['documents']:
            df_s = pd.DataFrame(document, index=[0])[['place_name','road_address_name', 'distance', 'x', 'y']]
            df = df.append(df_s)
        if json_obj['meta']['is_end'] == False:
            page += 1
        else:
            vl = QgsVectorLayer("Point?crs=EPSG:4326", "CVS", "memory")
            pr = vl.dataProvider()
            pr.addAttributes([QgsField("place_name", QVariant.String),
                              QgsField("road_address_name", QVariant.String),
                              QgsField("distance",  QVariant.Int),
                              QgsField("lon", QVariant.Double),
                              QgsField("lat", QVariant.Double)])
            vl.updateFields()
            for i in range(len(df)):
                f = QgsFeature()
                f.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(float(df.iloc[i, 4]), float(df.iloc[i, 3]))))
                f.setAttributes([df.iloc[i, 0], df.iloc[i, 1], df.iloc[i, 2], df.iloc[i, 4], df.iloc[i, 3]])
                pr.addFeature(f)
            vl.updateExtents()
            QgsProject.instance().addMapLayer(vl)
            break