'''
[실습 목표]
1. 터미널에서 pip install로 외부 라이브러리(Faker) 설치하기
2. 설치한 라이브러리를 import하여 가짜 데이터 생성하기
'''

# -------------------------------------------------
# 0. 라이브러리 설치 (필수!)
# -------------------------------------------------
# VS Code 하단 터미널(Terminal) 창에 아래 명령어를 입력하고 엔터를 치세요.
# pip install faker

# -------------------------------------------------
# 1. 라이브러리 가져오기
# -------------------------------------------------
from faker import Faker

# Faker 객체 생성 (한국어 데이터: 'ko_KR')
# 영어를 원하시면 'en_US'를 넣거나 비워두면 됩니다.
fake = Faker('ko_KR')

print("--- 🕵️‍♂️ 가짜 프로필 생성기 ---")

# 2. 가짜 데이터 생성해보기
# 실행할 때마다 매번 다른 데이터가 나옵니다.
name = fake.name()
address = fake.address()
email = fake.email()
job = fake.job()

print(f"이름: {name}")
print(f"주소: {address}")
print(f"이메일: {email}")
print(f"직업: {job}")

print("-" * 30)

# 3. [활용] 가짜 회원 3명 만들기
# 테스트용 데이터가 많이 필요할 때 아주 유용합니다.
print("--- 👥 가짜 회원 리스트 ---")

for i in range(3):
    print(f"[{i+1}번 회원]")
    print(f"이름: {fake.name()}")
    print(f"전화: {fake.phone_number()}")
    print(f"회사: {fake.company()}")
    print() # 줄바꿈