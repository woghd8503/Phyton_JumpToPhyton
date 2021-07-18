# If
money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
# 1. 들여쓰기 줄을 정렬 2. :을 꼭 붙인다.

# If 참과 거짓을 판단하는 문장
money = True
if money:
    print("돈이 있음")

# If 비교연산자
x = 3
y = 2
x > y
print(x > y)

x < y
print(x < y)

x == y
print(x == y)

x != y
print(x != y)

money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# If and, or, not
money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# If x in s, x not in s
1 in [1, 2, 3]
print(1 in [1, 2, 3])

1 not in [1, 2, 3]
print(1 not in [1, 2, 3])

'a' in ('a', 'b', 'c')
print('a' in ('a', 'b', 'c'))
'j' not in 'python'
print('j' not in 'python')

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

# If 다양한 조건을 판단하는 elif
pocket = ['paper', 'handphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
else:
    if card:
        print("택시를 타고 가라")
    else:
        print("걸어가라")

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
elif card:
    print("택시를 타고가라")
else:
    print("걸어가라")

if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket: pass
else: print("카드를 꺼내라")

# If 조건부 표현식
score = 40

if score >= 60:
    message = "success"
else:
    message = "false"

print(message)

message = "success" if score >= 60 else "false"
print(message)