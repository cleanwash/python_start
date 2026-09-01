'''
[실습 목표]
1. break: 반복문을 즉시 탈출 (비상구)
2. continue: 이번 순서만 건너뛰고 다음 순서로 (스킵)
3. 시나리오: 커피 자판기 프로그램 만들기
'''

coffee_stock = 5  # 커피 재고량 (5잔)

print("--- ☕ 커피 자판기 가동 ---")

# 무한 루프: 손님이 올 때까지 계속 대기
while True:
    
    # 현재 재고 현황 출력
    print(f"\n[남은 커피: {coffee_stock}잔]")
    
    # 1. 돈을 입력받습니다. (숫자만 입력한다고 가정)
    try:
        money = int(input("돈을 넣어주세요 (가격: 300원): "))
    except ValueError:
        print("숫자만 입력해 주세요!")
        continue # 다시 입력 받으러 위로 점프!

    # 2. 돈이 부족한 경우 (continue 실습)
    if money < 300:
        print(f"돈이 부족합니다. {money}원을 돌려드립니다.")
        print(">> 커피를 주지 않고 다음 손님을 받습니다.")
        continue  # 밑에 있는 코드는 무시하고 다시 while문 처음으로 점프!

    # 3. 정상 판매 (300원 이상)
    # 위에서 continue를 만나면 이 코드는 실행되지 않습니다.
    print(f"커피를 줍니다. ☕ (거스름돈: {money - 300}원)")
    coffee_stock = coffee_stock - 1  # 재고 감소

    # 4. 재고 확인 및 종료 (break 실습)
    if coffee_stock == 0:
        print("\n⛔ 재고가 다 떨어졌습니다. 판매를 중지합니다.")
        break  # 반복문을 완전히 끝내고 밖으로 나갑니다!

print("--- 영업 종료 ---")