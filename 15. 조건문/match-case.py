# match - case -> 변수 이름을 반복해서 칠 필요가 없어서 깔끔하다 
# 단순히 값 비교 뿐만 아니라, 데이터의 구조도 검사가 가능하다. 

status = 400
match status:
    case 200:
        print('성공')
    case 404:
        print('페이지 없음')
    case 500:
        print('서버 오류')
    case _:
        print('기타 오류')

# 패턴 매칭 
command = ["go", "east"]

match command:
    # 1) 종료 명령어 (길이 1, 값이 "quit")
    case ["quit"]:
        print("게임을 종료합니다.")

    # 2) 이동 명령어 (길이 2, 첫 번째가 "go")
    # 두 번째 값을 direction 변수에 자동으로 담아줍니다! (바인딩)
    case ["go", direction]:
        print(f"{direction}쪽으로 이동합니다! 🏃")

    # 3) 아이템 획득 (길이 2, 첫 번째가 "get")
    case ["get", item]:
        print(f"{item}을(를) 획득했습니다! 🎒")

    # 4) 그 외 모든 명령어
    case _:
        print("알 수 없는 명령어입니다.")
