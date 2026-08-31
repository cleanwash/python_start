#파이썬에서는 const가 없다. 
#대문자로 쓰면 '바꾸지 말자'는 약속 

menu = '아메리카노'
price = 2000
count = 3

total = price * count
print(f'주문 :{menu}, 가격 : {total}원')

#변수 값 변경(재할당)
#가격 인상
price = 2500
total = price * count
print(f'주문 :{menu}, 가격 : {total}원') #변수 값이 바뀌어도 total은 바뀌지 않는다.

#상수(약속:대문자)
MAX_RATE = 0.1 #고정
tax = total * MAX_RATE
print(f'세금 : {tax}원') #변수 값이 바뀌어도 total은 바뀌지 않는다.