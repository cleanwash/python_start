def add(a,b):
    return a + b

def sub(a,b):
    return a - b


if __name__ == '__main__':
    print(f'덧 셈 : {add(10,20)}') #덧셈 : 30
# else:
#     print('calculator.py가 import 되어 사용됨')

'''
1. if __name__ == '__main__': 핵심 요약

역할: 파일이 직접 실행되었을 때만 특정 코드(테스트, 시작 로직 등)를 실행하고, 다른 파일에서 import할 때는 건너뛰게 만드는 안전장치입니다.

이름표(__name__) 부여 규칙:

직접 실행된 파일: __name__ = '__main__' (주인공 명찰)

import된 파일: __name__ = '모듈파일명' (예: 'calculator')

불변 키워드: __name__과 '__main__'은 사용자가 임의로 바꿀 수 없는 파이썬 고정 키워드(Dunder)입니다.
'''