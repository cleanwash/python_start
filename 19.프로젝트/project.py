'''
[실습 목표]
1. 함수를 사용하여 사칙연산 기능 구현하기
2. while True를 사용하여 프로그램이 계속 실행되도록 만들기
3. try-except를 사용하여 에러(문자 입력, 0 나누기) 방어하기
'''

# -------------------------------------------------
# 1. 기능 구현 (함수 정의)
# -------------------------------------------------
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    # 나눗셈은 0으로 나누면 에러가 나므로 주의해야 합니다.
    return a / b

# -------------------------------------------------
# 2. 메인 로직 (무한 루프)
# -------------------------------------------------
print("--- 🧮 죽지 않는 스마트 계산기 ---")
print("종료하려면 첫 번째 숫자에 'q'를 입력하세요.\n")

while True:
    # [안전 장치] 에러가 발생할 수 있는 곳을 감쌉니다.
    try:
        # A. 입력 받기
        user_input = input("첫 번째 숫자 (또는 q): ")
        
        # 종료 조건 확인
        if user_input == 'q':
            print("계산기를 종료합니다. 안녕히 가세요! 👋")
            break  # 반복문 탈출

        # 숫자 변환 (여기서 문자를 넣으면 ValueError 발생!)
        num1 = float(user_input)
        
        operator = input("연산자 (+, -, *, /): ")
        num2 = float(input("두 번째 숫자: "))

        # B. 계산 및 결과 처리
        result = 0 # 결과 담을 변수

        if operator == "+":
            result = add(num1, num2)
        elif operator == "-":
            result = sub(num1, num2)
        elif operator == "*":
            result = mul(num1, num2)
        elif operator == "/":
            # 0으로 나누면 여기서 ZeroDivisionError 발생!
            result = div(num1, num2)
        else:
            print("⚠️ 올바른 연산자를 입력해주세요! (+, -, *, /)")
            continue # 다시 처음으로 돌아감

        # C. 결과 출력
        print(f"결과: {num1} {operator} {num2} = {result}")
        print("-" * 30)

    # [예외 처리] 에러별 대응
    except ValueError:
        print("⚠️ 에러: 숫자를 입력해야 합니다!")
    
    except ZeroDivisionError:
        print("⚠️ 에러: 0으로는 나눌 수 없습니다!")

    except Exception as e:
        print(f"⚠️ 알 수 없는 에러가 발생했습니다: {e}")