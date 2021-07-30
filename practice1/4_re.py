import re

p = re.compile("ca.e") 
# . : 하나의 문자를 의미 ca*e, care cade case cave 
# ^ : 문자열의 시작 ^de = desk desti~  (O)   fade(X)
# $ : 문자열의 끝 se$  = case  base (O)    sell (X)

#print(m.group()) #매치되지않으면 에러발생 

def print_match(m):
    if m:
        print("m.group():", m.group()) # 일치하는 문자열 반환
        print("m.string:", m.string) #입력받은 문자열 
        print("m.start():", m.start()) # 일치하는 문자열의 시작 index
        print("m.end():", m.end()) # 일치하는 문자열의 끝 index
        print("m.span():", m.span()) #일치하는 문자열의 시작 / 끝 index
    else:
        print("매칭되지 않음")

# m = p.search("good care")
# print_match(m) 

# m = p.search("good care") #search : 주어진 문자열 중 일치하는게 있는 지 확인 
# print_match(m)

# lst = p.findall("good care cafe") # findall 일치하는 모든 것을 리스트 형태로 반환
# print(lst)

# 1.  p = re.compile("원하는 형태")
# 2.  m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는 게 있는지 확인
# 3.  m = p.search("비교할 문자열") :
# 4.  