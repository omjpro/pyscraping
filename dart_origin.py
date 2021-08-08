import urllib.request
import zipfile
from bs4 import BeautifulSoup

K = "029843b831a12ee657729f3018c12624ae86d029"

url = "https://opendart.fss.or.kr/api/corpCode.xml?crtfc_key={K}".format(K=K)
urllib.request.urlretrieve(url, "firmlist.zip")

with zipfile.ZipFile("firmlist.zip") as zip_ref:
    zip_ref.extractall()

FM = open('CORPCODE.xml', encoding='utf-8').read()

B = BeautifulSoup(FM, 'lxml')

corpcode = B.find_all("corp_code")
stockcode = B.find_all("stock_code")
firmname = B.find_all("corp_name")

RLT = dict()
for C, S, F in zip(corpcode, stockcode, firmname):
    stock = S.get_text().strip()
    fcode = C.get_text().strip()
    name = F.get_text().strip()
    if stock == "":
        continue
    RLT[fcode] = (stock, name)

print(RLT)