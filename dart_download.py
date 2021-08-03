import urllib
import urllib.request

today = 20210803
market = "Y" #Y=kospi, K=kosdaq

K = "029843b831a12ee657729f3018c12624ae86d029"

url = "https://opendart.fss.or.kr/api/list.json?crtfc_key={K}&pblntf_detail_ty={f}&bgn_de={s1}&end_de={s2}&page_no=1&page_count=100".format(K=K, f=formtypecode, s1=begdate, s2=enddate)