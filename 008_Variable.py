# Variable
a = 1
b = "python"
c = [1,2,3]
print(a, b, c)

# Variable 변수란?
a = [1,2,3]
id(a)
print(id(a))  #메모리 주소

# Variable 리스트를 복사하고자 할 때
a = [1,2,3]
b = a
print(b)

id(a)
print(id(a))

id(b)
print(id(b))

a is b
print(a is b)

a[1] = 4
print(a)
print(b)

# Variable [:]이용
a = [1,2,3]
b = a[:]  # 전체 복사
a[1] = 4
print(a)
print(b)

# Variable copy 모듈 이용
from copy import copy
a = [1,2,3]
b = copy(a)
print(b)

b is a
print(b is a) # 두 변수가 같은 값을 가지면서 다른 객체를 제대로 생성했는지 확인 결과: false

a = [1,2,3]
b = a.copy()
print(b is a)

# Variable 변수를 만드는 여러 가지 방법
a, b =('phyton', 'life')
print(a, b)

(a, b) = 'python', 'life'
print((a, b))

a = b = 'python'
print(a)

a = 3
b = 5
a, b = b, a
print(a)
print(b)