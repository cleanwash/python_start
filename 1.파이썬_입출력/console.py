name = '코딩하는 기술사'

print('안녕' + name + '야')
# python에 f String을 사용하면 문자열 연결이 가능하다.
# 변수를 중괄호 안에 넣어주면 된다.
print(f'안녕 {name}야') #안녕 코딩하는 기술사야
print(f'안녕 {1+1}야') #안녕 2야

name = input('이름을 입력하세요: ')
print(f'안녕{name}야')

age = input('나이를 입력하세요: ')
age = int(age) + 1 # 따라서, int()를 붙여줘야 된다.
# TypeError: can only concatenate str (not "int") to str
print(f'나이가 {age}군요')

