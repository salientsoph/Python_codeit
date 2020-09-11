# 변수 이해하기
name = "소망"
x = 7
x = x + 1    # = 는 지정연산자로, 오른쪽을 왼쪽 변수에 지정하라는 뜻


# 함수의 실행 순서
# 윗줄부터 순서대로 실행
def hello():
    print("Hello!")
    print("Welcome to Python!")
print("함수 호출 전")
hello()
print("함수 호출 후")

def square(x):
    return x * x
print("함수 호출 전")
print(square(3) + square(4))
print("함수 호출 후")



# return문 이해하기
# return: (함수가) 무언가를 돌려주는 것
# 1. 값 돌려주기
# 2. 함수 즉시 종료하기
def square(x):
    print("함수 시작")
    return x * x
    print("함수 끝") # 사용될 일이 없음 -> "dead code"(의미없는 코드)
print(square(2))
print(square(3) + square(4))



# print vs return

def print_square(x):  # def print_square(3)
    print(x * x)  # print(3 * 3)

def return_square(x):  # def return_square(3)
    return x * x  # return 3 * 3

print_square(3)  # 9 출력
return_square(3)  # 9 로 대체됨(출력x)
print(return_square(3))  # 9 출력
print(print_square(3)) # 9, None 출력
# 안에 있는 부분을 먼저 계산함 -> print_square(3) -> 9 출력
# 함수 안에 리턴값이 없으므로 None을 리턴 -> print(None)



# [옵셔널 파라미터]
# 파라미터에게 default value(기본값)을 설정한 경우
# 기본값을 설정해 두면, 함수를 호출할 때 꼭 파라미터에 값을 안 넘겨 줘도 된다
# 필수로 넘겨 줄 필요가 없으니까 '옵셔널'이라고 함

def myself(name, age, nationality="한국"):
    print("내 이름은 %s" % name)
    print("나이는 %d살" % age)
    print("국적은 %s" % nationality)
myself("코드잇", 1, "미국")  # 옵셔널 파라미터를 제공하는 경우
print()  # 개행(= "\n")
myself("코드잇", 1)  # 옵셔널 파라미터를 제공하지 않는 경우


# 옵셔널 파라미터는 꼭 마지막에!
# 참고로 옵셔널 파라미터는 모두 마지막에 있어야 한다
# 아래처럼 옵셔널 파라미터를 중간에 넣으면 오류가 나온다!

# def myself(name, nationality="한국", age):
#     print("내 이름은 %s" % name)
#     print("나이는 %d살" % age)
#     print("국적은 %s" % nationality)

# 결과
# File "myself.py", line 1
#      def myself(name, nationality = "한국", age):
#                ^
# SyntaxError: non-default argument follows default argument



# scope(범위): 변수가 사용 가능한 범위

# 로컬변수: 함수 내에서 정의한 변수 -> 그 함수 내에서만 사용 가능한 변수
# 글로벌변수: 함수 밖에서 정의한 변수 -> 모든 곳에서 사용 가능한 변수
# 함수에서 변수를 사용하는 경우: 로컬변수 유무 먼저 확인 -> 글로벌변수 유무 확인

# 로컬변수만 있는 경우
def my_function():
    y = 3
    print(y)
my_function()  # 3 출력
# print(y)  # 오류 발생(y는 정의된 적 없음)

# 글로벌변수만 있는 경우
y = 2
def my_function2():
    print(y)
my_function2()  # 2 출력
print(y)  # 2 출력

# 로컬변수, 글로벌변수 둘 다 있는 경우
z = 2
def my_function3():
    z = 3
    print(z)
my_function3()  # 3 출력(가장 최근에 지정한 값)
print(z)  # 2 출력

# 파라미터도 로컬변수!
def square(x):
    return x * x
print(square(3))  # 3을 파라미터(x)로 넘겨줌(로컬변수로 작용)



# 상수(constant): 절대 바뀌지 않는 값
# 규칙: 이름을 지을 때 모든 글자를 대문자로
# (to 일반 변수랑 구분짓기, 실수하지 않기위해(값을 바꾸지 않기위함))

# 여기서 변수는 2개(pi, radius)
# PI는 고정값(상수), radius는 값이 계속 바뀜
PI = 3.14

# 반지름을 받아서 원의 넓이를 계산
def calculate_area(r):
    return PI * r * r

radius = 4
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))
radius = 6
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))
radius = 7
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))



# 스타일
# 이해하기 쉬운 코드 = 좋은 스타일을 가진 좋은 코드

# 안 좋은 스타일의 코드
print(6.28*4)
print(3.14*4*4)
print(6.28*8)
print(3.14*8*8)


# 좋은 스타일의 코드

# 변수 이름도 제대로!
# 상수는 대문자로
# 띄어쓰기, 개행 ("white space")
# 누구나 알 수 있도록 설명(함수로 만들기, 코멘트 설정 등)
# PEP8 규칙을 따른다
PI = 3.14  # 원주율(파이)

# 반지름이 r인 원의 둘레 계산
def calculate_circumference(r):
    return 2 * PI * r

# 반지름이 r인 원의 넓이 계산
def calculate_area(r):
    return PI * r * r

radius = 4  # 반지름
print(calculate_circumference(radius))
print(calculate_area(radius))

radius = 8  #반지름
print(calculate_circumference(radius))
print(calculate_area(radius))


