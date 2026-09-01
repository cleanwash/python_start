'''
[실습 목표]
1. 리스트와 문자열을 for문으로 하나씩 꺼내기 (순회)
2. enumerate() 함수를 사용하여 번호(Index)와 값(Value) 동시에 꺼내기
'''

# 1. 리스트 순회 (장바구니 털기)
# range(len(basket)) 같은 복잡한 방식 대신, 이렇게 직관적으로 씁니다.
basket = ["사과", "바나나", "포도"]

print("--- 장바구니 목록 ---")
for item in basket:
    print(f"꺼낸 과일: {item}")

print("-" * 30)

# 2. 문자열 순회 (한 글자씩)
# 문자열도 컨테이너(시퀀스)라서 for문에 바로 넣을 수 있습니다.
message = "Hello"

print("--- 문자열 분해 ---")
for char in message:
    print(f"글자: {char}") # 글자: H, 글자: e, 글자: l, 글자: l, 글자: o

print("-" * 30)

# 3. [핵심] enumerate() 활용
# 값만 나오니까 몇 번째인지 모르겠죠? 번호표가 필요할 때 씁니다.
# index는 0부터 시작하므로, 보기 좋게 +1을 해줍니다.
print("--- 번호표 붙이기 ---")

for index, item in enumerate(basket):
    print(f"{index + 1}번 과일: {item}")

print("-" * 30)

# 4. [응용] 점수 분석기
# 60점 이상인 학생만 "합격" 출력하기
scores = [80, 40, 90, 55]

print("--- 합격자 명단 ---")
for i, score in enumerate(scores):
    if score >= 60:
        print(f"{i + 1}번 학생: {score}점 (합격!)")


'''
방법 1: range(len()) (옛날 방식, 코드 주석에서 이미 언급됨)

for i in range(len(basket)):
    print(f"{i+1}번 과일: {basket[i]}")

방법 2: 수동으로 카운터 변수 만들기

count = 0
for item in basket:
    print(f"{count+1}번 과일: {item}")
    count += 1

방법 3: enumerate() (제일 파이썬스러운 방법, 추천됨)

for index, item in enumerate(basket):
print(f"{index+1}번 과일: {item}")
 '''