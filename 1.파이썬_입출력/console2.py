name = input('이름을 입력해주세요')
year = input('몇 년 생인가요?')
year = int(year)
age = 2025 - year +1 

#숫자 계산을 할 거면 반드시 -> int()처리를 해줘야 된다. 
print(f'{name}님은 {age}시군요')
