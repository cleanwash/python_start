# -------------------------------------------------
# 1.d
# -------------------------------------------------
def secret_room():
    # 함수 안에서 만든 변수
    secret = "비밀 문서"
    print(f"[함수 안] 접근 가능: {secret}")

secret_room()

# 함수 밖에서 부르면? -> 에러 발생!
# print(f"[함수 밖] 접근 시도: {secret}") # NameError: name 'secret' is not defined
print("[함수 밖] 지역 변수 'secret'은 보이지 않습니다.")

print("-" * 30)

# -------------------------------------------------
# 2. 전역 변수 (Global Variable) - 광장
# -------------------------------------------------
# 함수 밖에서 만든 변수
public_info = "공지사항"

def public_square():
    # 함수 안에서도 전역 변수는 잘 보입니다. (읽기 가능)
    print(f"[함수 안] 전역 변수 읽기: {public_info}")

public_square()
print(f"[함수 밖] 전역 변수 읽기: {public_info}")

print("-" * 30)

# -------------------------------------------------
# 3. 전역 변수 수정하기 (global 키워드)
# -------------------------------------------------
count = 0  # 전역 변수

def increase_count():
    global count  # 전역 변수 count를 사용하겠다고 명시
    count = count + 1  # 전역 count와 함수 내 count는 이름도 같고, 완전히 동일한 주소(같은 변수)다!
    print(f"[함수 안] 카운트 증가: {count}")

increase_count()
print(f"[함수 밖] 변경된 카운트: {count}")
