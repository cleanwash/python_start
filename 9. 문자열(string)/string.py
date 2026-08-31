#문자열의 구조 
#문자열은 문자들이 순서대로 연결된 기차입니다. HELLO -> 01234 
#[0:2] -> 시작과 끝 번호를 입력하면, 0번부터 1번까지 맨 뒤에 것은 먹히지 않는다. 

str1 = 'Hello'
str2 = "Python"
print(str1)
print(str2)

print('-'* 20) # 구분선 잘 나옴

#문자열 연산 
print('안녕' + '하세요')
print('ㅋ' * 3) #ㅋㅋㅋ

#길이와 인덱싱 
text='Hello'
print(f'원본 {text}')
print(f'길이 {len(text)}') 
print(f'첫 번째 글자[0] {text[0]}') #H
print(f'마지막 글자[-1] {text[-1]}') #o

#슬라이싱
#[시작:끝] -> 끝 번호는 포함 안됨 
print(f'앞 2글자 [0:2]: {text[0:2]}') #He