#True False라는 형태로 쓴다. 
#불리언은 내부적으로는 숫자 타입이다. 

#None타입은 -> 아무것도 없는 의미 -> 0이나 빈 문자와는 다른 의미 
#진공 상태-> 값이 정해지지 않았거나, 없음을 표현한다고 이해하면 될 것 같다. 


#boolean
is_ready = True
print(is_ready, type(is_ready)) #True <class 'bool'>

print(True + True + True -False) #3

#None
my_weapon = None # '', 0과는 엄연히 다름
if my_weapon is None:
    print('공격: 맨주먹으로 하기!') #공격: 맨주먹으로 하기!

my_weapon = '엑스칼리버'
if my_weapon is not None:
    print(f'공격: {my_weapon}로 하기!') #공격: 엑스칼리버로 하기!
