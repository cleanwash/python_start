'''
[실습 목표]
1. 매개변수(Parameter)로 함수에 데이터 전달하기
2. return을 사용하여 함수의 결과값 돌려받기
3. [주의] print만 있는 함수와 return이 있는 함수의 차이점 확인
'''

# 1. 매개변수 (데이터 받기)
# 외부에서 이름을 받아서 인사하는 함수
def say_hello(name):
    print(f"반갑습니다, {name}님!")

# 호출할 때 괄호 안에 데이터를 넣어줍니다. (인수)
say_hello("철수")
say_hello("영희")

print("-" * 30)

# 2. 반환값 (결과 돌려주기) - 더하기 기계
def add(a, b):
    result = a + b
    return result  # 계산 결과를 호출한 곳으로 던져줍니다!

# 리턴된 값은 변수에 '저장'해서 계속 쓸 수 있습니다.
sum_1 = add(10, 20)  # 30이 반환되어 저장됨
sum_2 = add(5, 5)    # 10이 반환되어 저장됨

print(f"첫 번째 결과: {sum_1}")
print(f"두 번째 결과: {sum_2}")
print(f"두 결과를 더하면? {sum_1 + sum_2}") # 재사용 가능!

print("-" * 30)

# 3. [함정 탈출] print vs return
def no_return_add(a, b):
    print(f"화면에만 보여줍니다: {a + b}")
    # return이 없으면 파이썬은 자동으로 None을 반환합니다.

# 변수에 담아볼까요?
value = no_return_add(3, 7)
print(f"변수에 저장된 값: {value}") # None
# print("값에 10을 더하면?", value + 10) # 에러 발생! (None + 10 불가능)