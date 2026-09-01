'''
파이썬 딕셔너리(Dictionary) 타입을 이해한다
딕셔너리를 사용하는 이유와 사용법을 숙지한다
'''
#dic.get('없는 키) => 에러 대신 None 반환
# 1. 딕셔너리 만들기 
my_profile = {
    "name" :"파이썬", 
    "age" :25, 
    "hobby" : "코딩"
}
print(f'딕셔너리 : {my_profile}') #딕셔너리 : {'name': '파이썬', 'age': 25, 'hobby': '코딩'}
print(f'타입: {type(my_profile)}') #타입: <class 'dict'>

#조회하기 
print(f'이름 : {my_profile["name"]}') #이름 : 파이썬
print(f'나이: {my_profile["age"]}') #나이: 25
print(f'이메일 : {my_profile.get("email")}') #이메일: None 

#3. 추가 및 수정하기 
#키가 있으면 수정, 없으면 새로운 키가 추가됩니다. 
my_profile['age'] =30 # 수정
my_profile['job']  = '개발자' #추가
print(f'수정 후 딕셔너리 : {my_profile}') #수정

#4. 삭제하기
del my_profile['hobby'] #삭제
print(f'삭제 후 딕셔너리 : {my_profile}') #삭제 후 �딕셔너리 : {'name': '파이썬', 'age': 30

#5. key와 value만 따로 보기
print(f'키 목록: {my_profile.keys()}') #키 목록: dict_keys(['name', 'age', 'job'])
print(f'값 목록: {my_profile.values()}') #값 목록: dict_values([' 파이썬', 30, '개발자'])