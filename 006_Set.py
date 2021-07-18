# Set
s1 = set([1, 2, 3])
print(s1)

s2 = set("Hello")
print(s2) #중복을 허용하지 않음, 순서가없다. 따라서 뒤죽박죽으로 출력

# Set 집합 자료형의 특징
s1 = set([1,2,3])
l1 = list(s1)
print(l1)
print(l1[0])

t1 = tuple(s1)
print(t1)
print(t1[0])

# Set 교집합
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

s1 & s2
print(s1 & s2)
print(s1.intersection(s2))

# Set 합집합
s1 | s2
print(s1 | s2)
print(s1.union(s2))

# Set 차집합
s1 - s2
print(s1 - s2)

s2 - s1
print(s2 - s1)

s1.difference(s2)
print(s1.difference(s2))

s2.difference(s1)
print(s2.difference(s1))

# Set 집합 자료형 관련 함수들
s1 = set([1, 2, 3])
s1.add(4)
print(s1)

# Set 값 여러 개 추가하기(update)
s1 = set([1, 2, 3])
s1.update([4, 5, 6])
print(s1)

# Set 특정 값 제거하기(remove)
s1 = set([1, 2, 3])
s1.remove(2)
print(s1)