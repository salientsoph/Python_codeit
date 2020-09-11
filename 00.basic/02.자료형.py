# 숫자형(Number) 연산

# 덧셈
print(4 + 7)
# 뺄셈
print(2 - 4)
# 곱셈
print(5 * 3)
# 나머지
print(7 % 3) # 7을 3으로 나눈 나머지(=1)
# 거듭제곱
print(2 ** 3)  # 2^3

# 혼합: 사칙연산을 따름
print(2 + 3 * 2)
print((2 + 3) * 2)

# 소수형의 연산 -> 결과도 모두 소수형
print(4.0 + 7.0)
print(2.0 - 4.0)
print(5.0 * 3.0)
print(7.0 % 3.0) # 7을 3으로 나눈 나머지(=1)
print(2.0 ** 3.0)  # 2^3
print("---------------------------")

# 정수형 & 소수형의 연산 -> 결과값이 모두 소수형
# 우선순위: 소수형 > 정수형
print(4 + 7.0)
print(2 - 4.0)
print(5 * 3.0)
print(7 % 3.0)  # 7을 3으로 나눈 나머지(=1)
print(2 ** 3.0)  # 2^3
print("---------------------------")

# 나눗셈: 결과값이 무조건 소수형
print(7 / 2)
print(6 / 2)
print(7.0 / 2)
print(6.0 / 2.0)
print("---------------------------")

# floor division(버림 나눗셈): 결과값이 무조건 정수형
print(7 // 2)
print(8 // 3)
print(8.0 // 3)  # 어느 하나라도 소수형이면 -> 결과도 소수형
print(8.0 // 3.0)  # 이것도 결과가 소수형
print("---------------------------")

# round(반올림): 가장 가까운 정수값으로 반올림
print(round(3.1415926535))
print(round(3.1415926535, 2))  # 소수점 2째자리까지 반올림
print(round(3.1415926535, 4))  # 소수점 4째자리까지 반올림
print("---------------------------")


# 문자열 연산
# 문자열(String): 키보드로 쓸 수 있는 문자들을 표현하는 자료형
# ' '  or  "  " -> 따옴표로 감싸준다
# '  "  or  "  '  -> 불가
print("파이썬")
print("화이팅")

print("I'm excited to learn Python!")
# print('I'm excited to learn Python!')  -> 오류
print('I\'m excited to learn Python!')  # 따옴표 안의 따옴표 앞에 \ 표기

print("Hello" + "world")
print("Hello" * 3)
print("3" + "5")
print("---------------------------")


# type conversion(형 변환): 값을 한 자료형에서 다른 자료형으로 바꾸는 것
print(int(3.8))  # int 정수
print(float(3))   # float 소수
print(int("2") + int("5"))
print(float("1.1") + float("2.5"))
print(str(2) + str(5))
# print(int("Hello world!"))  -> 오류(논리적 불가)
print("---------------------------")



# [문자열 + 숫자형 연산]

# age = 7
# print("제 나이는" + age + "살 입니다.")   -> 오류(문자열+숫자형 -> 불가)

age = 7
print("제 나이는" + str(age) + "살 입니다.")



# [syntatic sugar]
# 자주 쓰이는 표현을 더 간략하게 쓸 수 있게 해주는 문법

x = 0

# 다음 두 줄은 같습니다
x = x + 1
x += 1

# 다음 두 줄은 같습니다
x = x + 2
x += 2

# 다음 두 줄은 같습니다
x = x * 2
x *= 2

# 다음 두 줄은 같습니다
x = x - 3
x -= 3

# 다음 두 줄은 같습니다
x = x / 2
x /= 2

# 다음 두 줄은 같습니다
x = x % 7
x %= 7




# 1. format method(자주씀)
# -> 중괄호를 주고, 뒤에서 파라미터로 순서대로 받음

# 오늘은 2019년 10월 29일 입니다.
year = 2019
month = 10
day = 29
print("오늘은 " + str(year) + "년 " + str(month) + "월 " + str(day) + "일 입니다.")
print("오늘은 {}년 {}월 {}일 입니다.".format(year, month, day))

date_string = "오늘은 {}년 {}월 {}일 입니다."
print(date_string.format(year, month, day + 1))


# format 다루기

# 받는 format의 순서를 바꾸고 싶을 때
# (프로그래밍에선 0부터 센다!)
print("저는 {}, {}, {}를 좋아합니다.".format("딸기", "복숭아", "바나나"))
print("저는 {2}, {1}, {0}를 좋아합니다.".format("딸기", "복숭아", "바나나"))

num_1 = 1
num_2 = 3
print("{0} 나누기 {1}은 {2} 입니다.".format(num_1, num_2, num_1/num_2))
# 소숫점 2째자리까지 반올림
print("{0} 나누기 {1}은 {2:.2f} 입니다.".format(num_1, num_2, num_1/num_2))
# 소숫점 4째자리까지 반올림
print("{0} 나누기 {1}은 {2:.4f} 입니다.".format(num_1, num_2, num_1/num_2))
# 정수형으로 반올림
print("{0} 나누기 {1}은 {2:.0f} 입니다.".format(num_1, num_2, num_1/num_2))


# 2. % 기호(오래됨)
# %s(string:문자열), %d: "format string"
name = "사랑"
age = 10
print("제 이름은 %s이고 %d살입니다." % (name, age))


# 3. f-string(최신)
name = "행복"
age = 1000
print(f"제 이름은 {name}이고 {age}살 입니다.")



# [불 대수]
# 일상적인 논리를 수학적으로 표현한 것

# 일반 수학의 값: 숫자
# 일반 수학의 연산: +, - , *, /
# vs
# 불 대수의 값: 진리값(명제가 참인지, 거짓인지) -> True, False
# 불 대수의 연산: AND, OR, NOT

# 명제: 참과 거짓이 확실한 문장
# ex)
# 대한민국의 수도는 서울이다 -> 참인 명제
# 2는 1보다 작다 -> 거짓인 명제
# 한국의 수도는 어디일까요? -> 명제가 아님
# 코스모스는 예쁘다 -> 명제가 아님

# 1. and 연산
# x=True, y=True  ->  (x and y)=True
# x=False, y=True  ->  (x and y)=False
# 둘 중 하나라도 False이면 False
# 두 개 다 True여야만 True
# ex)
# 대한민국의 수도는 서울이다. AND 2는 1보다 크다
# = 대한민국의 수도는 서울이고, AND 2는 1보다 크다
# -> True

# 2. or 연산
# x=True, y=True  ->  (x or y)=True
# x=False, y=True  ->  (x or y)=True
# x=False, y=False  ->  (x or y)=False
# 둘 중 하나라도 True이면 True
# 두 개 다 False여야만 False
# ex)
# 대한민국의 수도는 제주이다. OR 대한민국의 수도는 서울이다.
# = 대한민국의 수도는 제주도거나 서울이다.
# -> True

# 3. not 연산
# x=True  ->  (not x)=False
# x=False  ->  (not x)=True
# ex)
# NOT 대한민국의 수도는 서울이다(True).
# = 대한민국의 수도는 서울이 아니다.
# -> False



# 불린(Boolean)
print(True)
print(False)

print("True")  # string
print("False")  # string

# and
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False
# or
print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False
# not
print(not True)
print(not False)
print("---------------------------")
print(2 > 1)
print(2 < 1)
print(3 >= 2)
print(3 <= 2)
print(2 == 2) # == (서로 같은 값)
print(2 != 2) # !=(같지 않다)
print(2 > 1 and "Hello" == "Hello")
print(not not True)
print(not not False)
print("---------------------------")
print(7 == 7 or (4 < 3 and 12 > 10))  # True or False
x = 3
print(x > 4 or not (x < 2 or x == 3)) # False or False



# type 함수: 어떤 자료형인지 확인
print(type(3))
print(type(3.0))
print(type("3"))
print(type("True"))
print(type(True))

def hello():
    print("Hello world!")
print(type(hello))
print(type(print))