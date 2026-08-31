'''
강제 사항은 아니다. 
정수: int, 
실수: float,
복소수: complex,
'''

num_int = 10
big_int = 21313211232131312
print(num_int, big_int)

num_int:int = 20
# num_int = '문자' #문자를 입력해도 상관이 없다. 하지만 타입 힌트가 있으므로, 정수형으로 사용해야 한다는 의미를 가진다.
print(type(num_int)) #str로 나온다. -> num_int='문자'를 주석을 하고 다시하니, int로 다시 바뀌어 잘 나온다. 

#실수 
num_float = 10.5
print(num_float, type(num_float)) #float

a=1 
b=1.0
print( a==b) #true 
print(type(a) ==type(b)) #false

#허수 주로 지도에서 자주 사용한다 -> 1은 가로, 2는 세로 위치로 쓰이는 경우가 많다.
num_complex = 1 + 2j
print(type(num_complex)) #complex

