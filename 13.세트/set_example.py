#1. 세트 만들기 
fruits = {'사과', '바나나', '체리', '사과'} 
print( f'세트 : {fruits}') #세트 : {'체리', '사과', '바나나'} => 중복 제거됨
#세트는 중복을 허용하지 않는다. 

#주의 -> 빈 세트를 만들어보기 
empty = {} #이건 딕셔너리 타입이다.
print(f'빈 세트 : {empty}') #빈 세트 : {}
print(f'빈 세트 타입 : {type(empty)}') #빈 세트 타입 : <class 'dict'>
empty = set() #이렇게 해야 빈 세트가 만들어진다.    
print(f'빈 세트 : {empty}') #빈 세트 : set()

#2. 세트 조작하기(추가/삭제)
#추가 
fruits.add('오렌지')
print(f'세트 : {fruits}') #세트 : {'체리', '사과', '바나나', '오렌지'}

#삭제 remove(), discard()
fruits.remove('바나나') #바나나 삭제
print(f'세트 : {fruits}') #세트 : {'체리', '사과', '오렌지'}
fruits.discard('망고') #fruits.remove('망고') #remove는 없는 값이면 에러 발생
print(f'세트 : {fruits}') #세트 : {'체리', '사과', '오렌지'}

#보통 set을 삭제할 때는, discard로 하는 것이 안전하다!

#3. 필살기 - 리스트 중복 제거 
numbers = [1,2,3,1,2,3,4,5]
#리스트 -> 셋트(중복제거) -> 리스트

unique_numbers = set(numbers) #중복 제거
print(f'중복 제거된 세트 : {unique_numbers}') #중복 제거된 세트 : {1, 2, 3, 4, 5}
unique_numbers = list(unique_numbers) #리스트로 변환
print(f'리스트로 변환 : {unique_numbers}') #리스트로 변환 : [1, 2, 3

#4. 집합 연산
team_A = {'철수', '영희', '민수'}
team_B = {'영희', '민수', '지수'}

#교집합
print(f'교집합 : {team_A & team_B}') #교집합 : {'영희', '민수'}
#합집합
print(f'합집합 : {team_A | team_B}') #합집합 : {'철수', '영희', '민수', '지수'}
#차집합
print(f'차집합 : {team_A - team_B}') #차집합 : {'철수'}