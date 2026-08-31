cart = ['사과', '바나나', '포도']

print(f'장바구니: {cart}')

print(f'첫 번째 담은 것[0]: {cart[0]}') #사과
print(f'마지막 담은 것[-1]: {cart[-1]}') #포도 

cart[1]= '옥수수'
cart.append('수박') #장바구니에 딸기 추가
print(f'장바구니: {cart}') #장바구니: ['사과', '옥수수', '포도', '수박']
print(f'[1:3] -> {cart[1:3]}') #['옥수수', '포도']

del cart[0]
print(f'삭제 후 장바구니 {cart}') #삭제 후 장바구니 ['옥수수', '포도', '수박']

print(len(cart)) #3