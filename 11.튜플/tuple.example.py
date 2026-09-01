# 튜플
my_tuple = (1,2,3)
print(f'튜플: {my_tuple}') #튜플: (1, 2, 3)
print(type(my_tuple)) #<class 'tuple'>

#괄호 없어도 가능 
no_bracket_tuple = 10, 20, 30 
print(f'괄호 없는 튜플: {no_bracket_tuple}') #괄호 없는 튜플: (10, 20, 30) => 괄호 없어도 괄호가 생김 -> 자동 패킹

#주의. 데이터가 1개일 때, 
not_tuple = (10) #괄호만 쓰면 그냥 숫자 10으로 인식
#값을 하나만 쓰고자 한다면 , 가 필수이다 (10,) -> 이런식으로 써야된다. 
print(f'괄호만 쓰면 그냥 숫자 10으로 인식: {type(not_tuple)}') 

#2. 불변성 (Immutable) -> 수정 불가 
# 조회(인덱싱)는 리스트와 동일하다. 
print(f'첫 번째 값 :{my_tuple[0]}') #첫 번째 값 :1  
print(f'두 번째 값 :{my_tuple[1]}') #두 번째 값 :2
print(f'세 번째 값 :{my_tuple[2]}') #세 번째 값 :3

# 수정하려고 한다면?-> 에러 발생 
#my_tuple[0] = 100 #TypeError: 'tuple' object does not support item assignment

#3. 튜플이 할 수 있는 일(조회)
data= (1,2,1,3,1)
print(f'1의 개수 : {data.count(1)}') #1의 개수 : 3

#index의 위치 
print(f'3의 위치 : {data.index(3)}') #3의 위치 : 3

# len
print(f'튜플의 길이 : {len(data)}') #튜플의 길이 : 5

#in: 포함 여부 확인(있냐?)
print(f'2가 있나요? : {2 in data}') #2가 있나요? : True
print(f'5가 있나요? : {5 in data}') #5가 있나요? : False

#4. 패킹 & 언패킹(Packing & Unpacking)
packed = 100, 200 
print(f'패킹된 튜플 : {packed}') #패킹된 튜플 : (100, 200)
a, b = packed
print(f'언패킹된 값 a : {a}, b : {b}') #언패킹된 값 a : 100, b : 200

# 꿀팁! 두 변수의 값 맞바꾸기(Swap)
# 다른 언어에서는 임시 변수(temp)가 필요하지만...

x = 5
y = 10
print(f'변경 전 x : {x}, y : {y}') #변경 전 x : 5, y : 10
x, y = y, x  # 두 값이 자동으로 스왑
print(f'변경 후 x : {x}, y : {y}') #변경 후 x : 10, y : 5