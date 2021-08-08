import sys

while True:   
    cho = int(input("""
    필요한 기능을 선택하세요:
    1. 새 메모 저장하기
    2. 메모 추가하기
    3. 메모 보기
    4. 종료하기
    """))
    if cho == 1:
        f = open("memo.txt", 'w')
        memo = input("메모를 작성하세요:")
        f.write(memo)
        f.write('/n')
        f.close()
    elif cho == 2:
        f = open("memo.txt", 'a')
        memo = input("추가 메모를 작성하세요:")
        f.write('/n')
        f.write(memo)
        f.close()
    elif cho == 3:
        f = open("memo.txt", 'r')
        memo = f.read()
        f.close()
        print(memo)
    elif cho == 4:
        break
    else :
        continue