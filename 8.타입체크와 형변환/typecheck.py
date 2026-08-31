print(type(10)) #int
print(type('10')) #str  

#형변환
num_str1 = '10'
num_str2 = '20'
print(num_str1 + num_str2) #1020

num_int1 = int(num_str1)
num_int2 = int(num_str2)
print(num_int1 + num_int2) #30

#실무 input()
a = input('첫 번쨰 숫자를 입력하세요: ')
b = input('두 번쨰 숫자를 입력하세요: ')
print(a + b) #100200

real_sum = int(a)+int(b)
print(real_sum) #300