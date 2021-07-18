# Tuple
t1 = ()
t2 = ()
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))
print(t1)
print(t2)
print(t3)
print(t4)
print(t5)

# Tuple 튜플 요솟값을 삭제하거나 변경하려고 할때
t1 = (1, 2, 'a', 'b')
#del t1[0] 에러 발생

t1 = (1, 2, 'a', 'b')

# Tuple 튜플 다루기 인덱싱하기
t1 = (1, 2, 'a', 'b')
t1[0]
print(t1[0])
t1[3]
print(t1[3])

# Tuple 슬라이싱 하기
t1 = (1, 2, 'a', 'b')
t1[1:]
print(t1[1:])

# Tuple 튜플 더하기
t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
t1 + t2
print(t1 + t2)

# Tuple 튜플 곱하기
t2 = (3, 4)
t2 * 3
print(t2 * 3)

# Tuple 튜플 길이 구하기
t1 = (1, 2, 'a', 'b')
len(t1)
print(len(t1))