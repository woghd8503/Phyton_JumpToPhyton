# Function

def add(a, b):
    return a + b

a = 3
b = 4
c = add(a, b)
print(c)

# Function parameter와 argument
def add(a, b):
    return a+b

print(add(3, 4))

# Function 입력값과 결괏값에 따른 함수의 형태
def add(a, b):
    result = a + b
    return result

a = add(3, 4)
print(a)

# Function 입력값이 없는 함수
def say():
    return 'Hi'
a = say()
print(a)

# Function 결괏값이 없는 함수
def add(a, b):
    print("%d, %d의 함은 %d입니다." % (a, b, a+b))
add(3, 4)
print(a)

# Function 매개변수 지정하여 호출하기
def add(a, b):
    return a+b
result = add(a=3, b=7)
print(result)

result = add(b=5, a=3)
print(result)

# Function 입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까?
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

result = add_many(1, 2, 3)
print(result)
result = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)

def add_mul(choice, *args):
    if choice == "add" :
        result = 0
        for i in args:
            result = result + i
    elif choice == "null":
        result = 1
        for i in args:
            result = result * i
        return result

result = add_many(1, 2, 3)
print(result)

result = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)

def add_mul(choice, *args):
     if choice == "add":
         result = 0
         for i in args:
             result = result + i
     elif choice == "mul":
         result = 1
         for i in args:
             result = result * i
     return result

result = add_mul('add', 1, 2, 3, 4, 5)
print(result)
result = add_mul('mul', 1, 2, 3, 4, 5)
print(result)

# Function 키워드 파라미터 kwargs
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a = 1)
{'a': 1}
print_kwargs(name='foo', age=3)
{'age': 3, 'name': 'foo'}

# Function 함수의 결괏값은 언제나 하나이다
def add_and_mul(a,b):
    return a+b, a*b

result = add_and_mul(3, 4)
print(result)

result1, result2 = add_and_mul(3, 4)
print(result1)
print(result2)

def add_and_mul(a,b):
    return a+b
    return a*b

# result = add_and_nul(2, 3)
# print(result)

# Function return의 또 다른 쓰임새
def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s 입니다." % nick)

say_nick('야호')
say_nick('바보')

# Function 매개변수에 초깃값 미리 설정하기
def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응용", 27)
say_myself("박응용", 27, True)

say_myself("박응선", 27, False)

# def say_myself(name, man=True, old):  매개변수 값 순서가 달라서 에러가 발생
#    print("나의 이름은 %s 입니다." % name)
#    print("나이는 %d살입니다." % old)
#    if man:
#        print("남자입니다.")
#    else:
#        print("여자입니다.")

# Function 함수 안에서 선언한 변수의 효력 범위

a = 1
def vartest(a):
    a = a + 1

vartest(a)
print(a)

def vartest(hello):
    hello = hello + 1

vartest(a)
print(a)

def vartest(a):
    a = a + 1
vartest(3)
print(a)

# Function 함수 안에서 함수 밖의 변수를 변경하는 방법

# return
a = 1
def vartest(a):
    a = a + 1
    return a

a = vartest(a)
print(a)

# global
a = 1
def vartest():
    global a
    a = a+1

vartest()
print(a)

# lambda
add = lambda a, b: a+b
result = add(3, 4)
print(result)

def add(a, b):
    return a+b

result = add(3, 4)
print(result)