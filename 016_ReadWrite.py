# RW 파일 생성하기
f = open("새파일.txt", 'w')
f.close()

f = open("D:/01.Coding_study/Pyton/Phyton_JumpToPython/새파일1.txt", 'w')
f.close()

# RW 파일을 쓰기 모드로 열어 출력값 적기
f = open("D:/01.Coding_study/Pyton/Phyton_JumpToPython/새파일1.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close

for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    print(data)

# 한 줄에 결괏값 출력하기
for i in range(10):
    print(i, end=' ')

# RW 프로그램의 외부의 저장된 파일을 읽는 여러가지 방법
# readline 함수 이용하기

f = open("D:/01.Coding_study/Pyton/Phyton_JumpToPython/새파일1.txt", 'r')
line = f.readline()
print(line)
f.close

f = open("D:/01.Coding_study/Pyton/Phyton_JumpToPython/새파일1.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

while True:
    data = input()
    if not data: break
    print(data)

# RW readlines 함수 사용하기
f = open("D:/01.Coding_study/Pyton/Phyton_JumpToPython/새파일1.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close

# RW 줄 바꿈(\n) 문자 제거하기
f = open("D:/01.Coding_study/Pyton/Phyton_JumpToPython/새파일1.txt", 'r')
lines = f.readlines()
for line in lines:
    line = line.strip # 줄 끝의 줄 바꿈 문자를 제거한다.
    print(line)
f.close()

# RW read 함수 사용하기
f = open("D:/01.Coding_study/Pyton/Phyton_JumpToPython/새파일1.txt", 'r')
data = f.read()
print(data)
f.close()

# RW 파일에 새로운 내용 추가하기
f = open("D:/01.Coding_study/Pyton/Phyton_JumpToPython/새파일1.txt", 'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# RW with문과 함께 사용하기
f = open("foo.txt", 'w')
f.write("Life is too short, you need python")
f.close()

with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")