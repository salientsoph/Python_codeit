# "코멘트"(주석): 실제 프로그램이 실행될 때 무시됨.
# <목적>
# 1. 복잡한 코드 설명
# 2. 하다가 만 부분 표시
# 3. 다른 개발자들과 소통
print("Hello world!") # 이것도 코멘트



# 자료형 개요

# 프로그래밍이란
# 계산할 수식들을 컴퓨터에게 알려주는 것

# 자료형(Data Type)
# 1. 숫자형
# 1) 정수(integer): -1, -2, -3, 0, 1, 2, 3
# 2) 소수(floating point): 3.14, -7.08, 2.0
# 파이썬은 2 와 2.0은 다르다

# 2. 문자열(string)
# "hello", "world", "2"
# 문자열도 계산 가능
print("hello" + "world")

# 2 : 정수
# 2.0 : 소수
# "2": 문자열
print(2+5)
print(2.0+5.0)
print("2"+"5")

# 3. 불린(boolean): 참과 거짓(True False)
print(7>3)
print(3>7)



# 추상화 개요

# 추상화(abstraction): 복잡한 내용은 숨기고, 주요 기능에만 신경 쓰는 것
# 변수(variable), 함수(function), 객체(object)

# 1.변수(variable): 값을 저장하는 것
x = 254
y = 317
print(x+y)

# 프로그래밍에서의 "="
# =(지정연산자): 오른쪽 값을 왼쪽 변수에 지정
burger_price = 4990
fries_price = 1490
drink_price = 1250

print(burger_price)
print(burger_price*2)
print(burger_price + fries_price)
print(burger_price * 3 + fries_price * 2 + drink_price * 5)


# 2.함수(function): 명령을 저장하는 것
# 내장함수: 프로그램을 만든 개발자들이 이미 구현해놓은 것
print("Hello world!")

# def 함수이름():    "함수의 헤더"
#(tab) 명령
def hello():
    print("Hello world!")
    print("Welcome to codeit!")
hello()
hello()
hello()


# 파라미터: 함수에 넘겨주는 값
# 파라미터 이름은 맘대로 바꿀 수 있음
def hello(name):  # name: 파라미터
    print("Hello world!")
    print(name)
    print("Welcome to codeit!")
hello("Chris")
hello("Michael")
# hello()  -> 에러남


# 여러개의 파라미터
def print_sum(a, b, c):
    print(a+b*c)
print_sum(7, 3, 4)


# return문(돌려줌)
# 어떤 정보를 주면, 계산된 값을 돌려줌
def get_square(x):
    return x * x
print(get_square(3))  # print(9)

y = get_square(3)
print(y)

print(get_square(3)) + print(get_square(4))

