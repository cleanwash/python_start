# 1. 기본값 매개변수 (Default Parameter)
# 자주 쓰는 값(Tall)을 미리 넣어두면, 매번 입력할 필요가 없습니다.
def order_coffee(menu, size="Tall"):
    print(f"주문하신 {menu}({size}) 나왔습니다.")

print("--- ☕ 카페 주문 ---")
order_coffee("아메리카노")           # size 안 넣음 -> "Tall" (자동)
order_coffee("카페라떼", "Grande")   # size 넣음 -> "Grande" (변경)

print("-" * 30)

# 2. 키워드 인자 (Keyword Arguments)
# 인자가 많을 때, 이름표를 붙여서 전달하면 순서를 외울 필요가 없습니다.
def make_profile(name, age, main_lang):
    print(f"이름: {name} / 나이: {age} / 언어: {main_lang}")

print("--- 👤 프로필 생성 ---")
# [기존 방식] 순서를 틀리면 큰일 납니다. (이름 자리에 나이를 넣으면?)
make_profile("김철수", 20, "파이썬")

# [키워드 방식] 순서가 뒤죽박죽이어도 정확하게 들어갑니다.
make_profile(age=25, main_lang="자바", name="이영희")

print("-" * 30)

# 3. [혼합 사용 & 꿀팁]
# 중간에 있는 기본값은 건너뛰고, 필요한 것만 콕 집어 바꿀 수 있습니다.

def buy_ticket(movie, price=12000, seat="랜덤"):
    print(f"예매: {movie} | 가격: {price}원 | 좌석: {seat}")

print("--- 🎫 영화 예매 ---")
buy_ticket("아이언맨")  # 기본값 사용
buy_ticket("아바타", seat="A-10")  # price(12000)는 그대로 두고, seat만 변경!

# [주의] 순서 규칙
# buy_ticket(seat="F-5", "슈퍼맨") # 에러! (키워드 뒤에 일반 값이 올 수 없음)
#순서가 제일 중요하다 -> 일반 변수가 항상 먼저(앞에)와야 한다. 