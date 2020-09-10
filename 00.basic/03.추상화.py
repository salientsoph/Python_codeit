# 변수 이해하기
name = "소망"
x = 7
x = x + 1    # = 는 지정연산자로, 오른쪽을 왼쪽 변수에 지정하라는 뜻


# 함수의 실행 순서
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



