# Class
print("사칙연산 함수")
result = 0

def add(num):
    global result
    result += num
    return result

print(add(3))
print(add(4))

result1 = 0
result2 = 0

print("사칙연산 함수1")
def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))

print("사칙연산 클래스")
class Calulator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calulator()
cal2 = Calulator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

# Class 사칙연산 클래스 만들기
#a = FourCal()
#a.setdata(4, 2)

#print(a.add())

#print(a.mul())

#print(a.sub())

#print(a.div())

# Class 클래스 구조 만들기
class FourCal:
    pass

a = FourCal()
type(a)
print(type(a))
#<class '__main__FourCal'>

# Class 객체에 숫자 지정할 수 있게 만들기
#a.setdata(4, 2)

class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

a = FourCal()
a.setdata(4, 2)
print(a.first)
print(a.second)

a = FourCal()
b = FourCal()

a.setdata(4, 2)
print(a.first)

b.setdata(3, 7)
print(b.first)

print(a.first)

a = FourCal()
b = FourCal()
a.setdata(4, 2)
b.setdata(3, 7)
id(a.first)
print(id(a.first))
id(b.first)
print(id(b.first))

class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

# Class 더하기 기능 만들기
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result

a = FourCal()
a.setdata(4, 2)
print(a.add())

# Class 곱하기, 빼기, 나누기 기능 만들기
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal()
b = FourCal()
a.setdata(4, 2)
b.setdata(3, 8)

a.add()
print(a.add())

a.mul()
print(a.mul())

a.sub()
print(a.sub())

a.div()
print(a.div())

b.add()
print(b.add())

b.mul()
print(b.mul())

b.sub()
print(b.sub())

b.div()
print(b.div())

# Class Constructor
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal(4, 2)
print(a.first)
print(a.second)

a = FourCal(4, 2)
print(a.add())
print(a.div())

# Class 클래스의 상속
class MoreFourCal(FourCal):
    pass

a = MoreFourCal(4, 2)
a.add()
print(a.add())
a.mul()
print(a.mul())
a.sub()
print(a.sub())
a.div()
print(a.div())

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4, 2)
a.pow()
print(a.pow())

# Class 메서드 오버라이딩
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
a = SafeFourCal(4, 0)
print(a.div())

# Class 클래스 변수
class Family:
    lastname = '김'

print(Family.lastname)

a = Family()
b = Family()
print(a.lastname)
print(b.lastname)

Family.lastname = "박"
print(a.lastname)
print(b.lastname)

print(id(Family.lastname))
print(id(a.lastname))
print(id(b.lastname))

