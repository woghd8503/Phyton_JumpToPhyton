# List odd
add = [1, 3, 5, 7, 9]
print(add)

# List 여러가지 생김새
a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short' ]
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]
print(a, b, c, d, e)

# List 리스트의 인덱시
a = [1, 2, 3]
print(a)

a[0]
print(a[0])

a[0] + a[2]
print(a[0] + a[2])

a[-1]
print(a[-1])

a = [1, 2, 3, ['a', 'b', 'c']]
print(a)

a[0]
print(a[0])
a[-1]
print(a[-1])
a[3]
print(a[3])

a[-1][1]
print(a[-1][1])
a[-1][2]
print(a[-1][2])

# List 삼중 리스트에서 인덱싱하기
a = [1, 2, ['a', 'b', ['Life', 'is']]]
print(a[2][2][0])

# List 리스트의 슬라싱
a = [1, 2, 3, 4, 5]
a[0:2]
print(a[0:2])

a ="12345"
a[0:2]
print(a[0:2])

a = [1, 2, 3, 4, 5]
b = a[:2]
c = a[2:]
print(b)
print(c)

# List 중첩된 리스트에서 슬라이싱하기
a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
a[2:5]
print(a[2:5])
a[3][:2]
print(a[3][:2])

# List 리스트 더하기(+)
a = [1, 2, 3]
b = [4, 5, 6]
a + b
print(a + b)

# List 리스트 반복하기(*)
a = [1, 2, 3]
a * 3
print(a * 3)

# List 리스트 길이구하기
a = [1, 2, 3]
len(a)
print(len(a))

# List 초보자가 범하기 쉬운 리스트 연산 오류
a = [1, 2, 3]
#a[2] + "hi" 에러발생
#print(a[2] + "hi")

str(a[2]) + "hi"
print(str(a[2]) + "hi")

# List 리스트에서 값 수정하기
a = [1, 2, 3]
a[2] = 4
print(a)

# List del 함수 사용해 리스 요소 삭제하기
a = [1, 2, 3]
del a[1]
print(a)

a = [1, 2, 3, 4, 5]
del a[2:]
print(a)

# List 관련 함수들 리스트에 요소 추가(append)
a = [1, 2, 3]
a.append(4)
print(a)

a.append([5, 6])
print(a)

# List 리스트 정렬(sort)
a = [1, 4, 3, 2]
a.sort()
print(a)

# List 리스트 뒤집기(reverse)
a = ['a', 'c', 'b']
a.reverse()
print(a)

# List 위치 반환(index)
a = [1, 2, 3]
a.index(3)
print(a.index(3))
a.index(1)
print(a.index(1))

# List 리스트에 요소 삽입(insert)
a = [1, 2, 3]
a.insert(0, 4)
print(a)

a.insert(3, 5)
print(a)

# List 리스트 요소 제거(remove)
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)

a.remove(3)
print(a)

# List 리스트 요소 끄집어내기(pop)
a = [1, 2, 3]
a.pop(1)
print(a)

# List 리스트에 포함된 요소 x의 개수 세기(count)
a = [1, 2, 3, 1]
a.count(1)
print(a.count(1))

# List 리스트 확장(extend)
a = [1, 2, 3]
a.extend([4,5])
print(a)
b = [6, 7]
a.extend(b)
print(a)