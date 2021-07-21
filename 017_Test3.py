# Q1 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.
number = input("숫자를 입력하세요: ")

def is_odd(a):
    if a % 2 == 0:
        return("입력하신 값은 짝수")
    if a % 2 != 0:
        return("입력하신 값은 홀수")

print(is_odd(int(number)))

# Q2 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자.(단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

print(avg_numbers(1, 2))
print(avg_numbers(1,2,3,4,5))

# Q3 3과 6을 입력했을 때 9가 아니 36이라는 결괏값을 돌려주었다. 이 프로그램의 오류를 수정해 보자.
input1 = input("첫 번째 숫자를 입력하세요:")
input2 = input("두 번재 숫자를 입력하세요:")


total = int(input1) + int(input2)
print("두수의 합은 %s 입니다" % total)

# Q4 다음 중 출력 결과가 다른 것 한 개를 고르시오.
print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python")
print("".join(["you", "need", "python"]))

# 답은 3번 you need python

# Q5 다음은 "text.txt"라는 파일에 "Life is too short" 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다.
f1 = open("test1.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("D:/01.Coding_study/Pyton/Phyton_JumpToPython/test1.txt", "r")
result = f2.readline()
print(result)
f2.close()

# Q6 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자.
a = input("저장할 내용을 입력하세요:")
f = open('D:/01.Coding_study/Pyton/Phyton_JumpToPython/text1.txt', 'a')
f.write(a)
f.write("\n")
f.close()

# Q7 다음과 같은 내용을 지닌 파일 test.txt가 있다. 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.

f = open("test2.txt", 'w')
f.write("I need java")
f.close()

f = open('D:/01.Coding_study/Pyton/Phyton_JumpToPython/test2.txt', 'r')
result = f.readline()
f.close()

result = result.replace('java', 'python')

f = open('test2.txt', 'w')
f.write(result)
f.close()