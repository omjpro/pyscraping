import urllib
import urllib.request

K = "029843b831a12ee657729f3018c12624ae86d029"
formtypecode = "A001"
begdate = '20210701'
enddate = '20210702'

URL = "https://opendart.fss.or.kr/api/list.json?crtfc_key={K}&pblntf_detail_ty={f}&bgn_de={s1}&end_de={s2}&page_no=1&page_count=100".format(K=K, f=formtypecode, s1=begdate, s2=enddate)

print(URL)

RLT = urllib.request.urlopen(URL)

D = RLT.read().decode("utf-8")
# #common encoding : "UTF-8", "euc-kr", "latin-1", "utf-16"

print(D)
