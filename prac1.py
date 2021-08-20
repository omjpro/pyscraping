coffee = 3
milk = 3
money = 17

while True:
    choice = input("""
    선택하세요
    1. 커피
    2. 우유
    3. 종료
    """)

    if coffee == 0 and milk == 0:
        print("재고가 모두 소진되었습니다")
        break

    elif money <= 3:
        print(f"잔액이부족합니다. 잔돈을 반환합니다. 잔돈 : {money}원")
        break
    else :
        if choice == '1':
            if coffee == 0:
                print("커피 재고가 없습니다")
                continue
            coffee -= 1
            money -= 3
            print("coffee")
            continue
        elif choice =='2':
            if milk == 0:
                print("우유 재고가 없습니다")
                continue
            milk -= 1
            money -= 3
            print("milk")
            continue

        elif choice == '3':
            break

        else :
            print("잘못선택하셨습니다")
            continue
        
        continue

