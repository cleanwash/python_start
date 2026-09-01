'''
[실습 목표]
1. try-except 구문으로 에러 발생 시 프로그램 종료 막기
2. ZeroDivisionError, ValueError 등 에러 종류별로 다르게 처리하기
3. finally 구문으로 무조건 실행되는 코드 작성하기
'''

print("--- 🧮 안전한 나눗셈 계산기 ---")

while True:
    try:
        # 1. 시도할 코드 (위험 구간)
        num_str = input("숫자를 입력하세요 (종료: q): ")
        
        if num_str == 'q':
            print("계산기를 종료합니다.")
            break
            
        num = int(num_str)          # ValueError 위험! (문자 넣으면 터짐)
        result = 10 / num           # ZeroDivisionError 위험! (0 넣으면 터짐)
        
        print(f"10 나누기 {num} = {result}")

    except ValueError:
        # 2. 숫자가 아닐 때 실행
        print("⚠️ 에러: 숫자만 입력해 주세요!")

    except ZeroDivisionError:
        # 3. 0으로 나눴을 때 실행
        print("⚠️ 에러: 0으로는 나눌 수 없습니다!")

    except Exception as e:
        # 4. 그 외 알 수 없는 에러
        print(f"알 수 없는 에러가 발생했습니다: {e}")

    finally:
        # 5. 성공하든 실패하든 무조건 실행
        print("--- 계산 시도 완료 ---\n")