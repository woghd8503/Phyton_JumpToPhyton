# String ""
food = "Python's favorite food is perl"
print(food)

# string ""를 출력하기 위해 '를 사용
say = '"Python is very easy." he says.'
print(say)

# String \를 이용해서 '와 "를 문자열 포함
food = 'Python\'s favorite food is perl'
print(food)

say = "\"Python is very easy.\" he says."
print(say)

# String 줄을 바꾸기위한 이스케이프 코드 \n
multiline = "Life is too short\n You need python"
print(multiline)

# String 작은 따음표 3개 ''' or 큰따옴표 3개 """
multiline = '''
Life is too short
You need Python
'''
print(multiline)

multiline = """
Life is too short
You need Python
"""
print(multiline)

# String Concatenation 문자열 연결하기
head = "Python"
tail = " is fun!"
head + tail
print(head + tail)

# String 문자열곱사기
a = "python"
a * 2
print(a * 2)

# String 문자열곱하기 응용
print("=" * 50)
print("My Program")
print("=" * 50)

# String 문자열 길이 구하기
a = "Life is too short"
len(a)
print(len(a))

# String 문자열 인덱싱
a = "Life is too short, You need Python"
a[3]
print(a[3])

# String 문자열 인덱싱 활용
a = "Life is too short, You need Python"
a[0]
print(a[0])
a[12]
print(a[12])
a[-1]
print(a[-1])
a[-2]
print(a[-2])
a[-5]
print(a[-5])

# String 문자열 슬라이싱
a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
print(b)

a[0:4]
print(a[0:4])
a[0:3]
print(a[0:3])

a[5:7]
print(a[5:7])
a[12:17]
print(a[12:17])

a[19:]
print(a[19:])
a[:17]
print(a[:17])
a[:]
print(a[:])
a[19:-7]
print(a[19:-7])

# String 슬라이싱으로 문자열 나누기
a = "20010331Rainy"
date = a[:8]
weather = a[8:]
print(date, weather)

# String Question Pithon -> Python으로 변경
a = "Pithon"
#a[1] = 'y'  오류발생
#print(a[1])


a = "Pithon"
print(a[:1] + 'y' + a[2:])

# String 포매팅 숫자 바로 대입
a = "I eat %d apples." % 3
print(a)

# String 문자열 바로 대입
a = "I eat %s apples." % "five"
print(a)

# String 숫자 값을 나타내는 변수로 대입
number = 3
a = "I eat %d apples." % number
print(a)

# String 2개 이상의 값 넣기
number = 10
day = "three"
a = "I ate %d apples. so I was sick for %s days." % (number, day)
print(a)

# String %포맷은 어떤 형태의 값이든 변환해 넣을 수 있다.
a = "I have %s apples" % 3
print(a)
a = "rate is %s" % 3.234
print(a)

# String %d와 %를 같이 쓸 때는 %%를 쓴다
#a = "Error is %d%." % 98 에러발생

a = "Error is %d%%." % 98
print(a)

# String 정렬과 공백
a = "%10s" % "hi"
print(a)

a = "%-10sjane." % 'hi'
print(a)

# String 소수점 표현하기 자릿수 만큼
a = "%0.4f" % 3.42134234
print(a)

a = "%10.4f" % 3.42134234
print(a)

# String format 함수를 사용한 포매팅
a = "I eat {0} apples". format(3)
print(a)

# String 문자열 바로 대입하기

a = "I eat {0} apples". format("five")
print(a)

# String 숫자 값을 가진 변수로 대입하기
number = 3
a = "I eat {0} apples". format(number)
print(a)

# String 2개 이상의 값 넣기
number = 10
day = "three"
a = "I ate {0} apples. so I was sick for {1} days.". format(number, day)
print(a)

# String 이름으로 넣기
a = "I ate {number} apples. so I was sick for {day} days.". format(number=10, day=3)
print(a)

# String 인덱스와 이름을 혼용해서 넣기
a = "I ate {0} apples. so I was sick for {day} days.". format(10, day=3)
print(a)

# String 왼쪽 정렬
a = "{0:<10}". format("hi")
print(a)

# String 오른쪽 정렬
a = "{0:>10}". format("hi")
print(a)

# String 가운데 정렬
a = "{0:=^10}". format("hi")
print(a)

a = "{0:!<10}". format("hi")
print(a)

# String 소주점 표현하기
y = 3.42134234
a = "{0:10.4f}". format(y)
print(a)

a = "{0:10.4f}". format(y)
print(a)

a = "{{ and }}". format()
print(a)

# String 문자열 문자 개수 세기(count) 관련 함수들
a = "hobby"
a.count('b')
print(a.count('b'))

# String 문자열 위치 알려주기(find)
a = "Python is the best choice"
a.find('b')
print(a.find('b'))
a.find('k')
print(a.find('k'))

# String 위치 알려주기(index)
a = "Life is too short"
a.index('t')
print(a.index('t'))

# String 문자열 삽입(join)
a = ",".join('abcd')
print(a)

# String 소문자를 대문자로 바꾸기(upper)
a = "hi"
a.upper()
print(a.upper())

# String 대문자를 소문자로 바꾸기(lower)
a = "HI"
a.lower()
print(a.lower())

# String 왼쪽 공백 지우기(lstrip)
a = " hi "
a.lstrip()
print(a.lstrip())

# String 오른쪽 공백 지우기(rstrip)
a = " hi "
a.rstrip()
print(a.rstrip())

# String 양쪽 공백 지우기(strip)
a = " hi "
a.strip()
print(a.strip())

# String 문자열 바꾸기(replace)
a = "Life is too short"
a.replace("life", "Your leg")
print(a.replace("Life", "Your leg"))

# String 문자열 나누기(split)
a = "Life is too short"
a.split()
print(a.split())
b = "a:b:c:d"
b.split(':')
print(b.split(':'))