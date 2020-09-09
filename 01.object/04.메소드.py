
# class User:
#     def initialize(self, name, email, password):
#         self.name = name
#         self.email = email
#         self.password = password

# 새 인스턴스를 만들 땐 코드 2줄만 쓰면 됨.
# 유저를 생성하는 줄 하나, 인스턴스 변수의 초기값을 설정하는 줄 하나.

# user1 = User()
# user1.initialize("Young", "young@codeit.kr", "123456")

# user2 = User()
# user2.initialize("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")

# user3 = User()
# User.initialize(user3, "Taeho", "taeho@codeit.kr", "123abc")

# user4 = User()
# User.initialize(user4, "Lisa", "lisa@codeit.kr", "abc123")

# print(user1.name, user1.email, user1.password)
# print(user2.name, user2.email, user2.password)
# print(user3.name, user3.email, user3.password)
# print(user4.name, user4.email, user4.password)



# __init__
# 메소드 이름 앞뒤로 __ 가 있는 메소드를 "매직 메소드", "스페셜 메소드"라고 함.("특수 메소드")
# 특수 메소드: 특정 상황에서 자동으로 호출되는 메소드
# double underscore(줄여서 "dunder" 메소드 라고 불리기도 함)
# __init__ 메소드: 인스턴스가 생성될 때 자동으로 호출됨

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

user1 = User("Young", "young@codeit.kr", "123456")
# 1. User 인스턴스 생성
# 2. __init__ 메소드 자동 호출
# --> __init__(self == user1, (괄호 안의 값들이 순서대로 들어감)"Young", "young@codeit.kr", "123456")
# --> __init__ 메소드는 인스턴스 변수들의 초깃값을 설정해줌
# --> 즉, init 메소드 사용시, <<유저를 생성하는 줄 하나, 인스턴스 변수의 초기값을 설정하는 줄 하나.>> 를 한 줄로 줄인다.


user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
user3 = User("Taeho", "taeho@codeit.kr", "123abc")
user4 = User("Lisa", "lisa@codeit.kr", "abc123")

print(user1.name, user1.email, user1.password)
print(user2.name, user2.email, user2.password)
print(user3.name, user3.email, user3.password)
print(user4.name, user4.email, user4.password)




print("-" * 30)





class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def say_hello(self):
        print("안녕하세요. 저는 {} 입니다.".format(self.name))

    def __str__(self):
        return "사용자: {}, 이메일: {}, 비밀번호: ****".format(self.name, self.email)



# 특수 메소드: 특정 상황에 자동으로 자동으로 호출되는 메소드
# "dunder str": print함수를 호출할 때 자동으로 불려와짐. print하면 str의 return값을 출력.

user1 = User("마루코", "marrrr@marzang.com", "1234")
user2 = User("하루", "haruuu@haru.com", "4567")

print(user1)
# str이 없을 시, <__main__.User object at 0x1053e9370> 라는 결과가 나옴.
# 즉, 이 경우 type와 메모리 주소가 나온다.
print(user2)




print("-" * 30)



# 클래스 변수: 여러 인스턴스들이 공유하는 속성, 한 클래스의 모든 인스턴스가 공유하는 속성
# 예를 들어 고객(인스턴스)의 총 갯수를 나타내는 변수를 표현할 때 count = 0으로 시작한다면,
# 어떤 유저 인스턴스라도 서로 똑같은 값을 가지고 있어야함.

class User:
    count = 0

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        User.count += 1
        # 유저 인스턴스가 생성될때마다 실행되는건 init 메소드 이므로, init에 count 포함시킴

user1 = User("딸기", "sss@sss.sss", "1234")
user2 = User("오렌지", "rrr@rrr.rrr", "3456")
user3 = User("망고", "ttt@ttt.ttt", "4567")

user1.count = 5
# 이건 인스턴스 변수를 설정할 때 쓰던 어문임. 이렇게 쓰면 user1의 count라는 인스턴스 변수가 생성.
# 즉 같은 이름의 인스턴스 변수를 생성한 것
# 같은 이름의 클래스 변수(User.count) vs 같은 이름의 인스턴스 변수(user1.count) 가 있다면
# ---> "인스턴스 변수"가 읽어짐
# 따라서 헷깔리지 않게!! 클래스 변수에 값을 설정할 때는 클래스 이름으로만! (User.count = 5) 이렇게.

# 클래스 변수의 값 설정하기
# only 클래스 이름.클래스 변수 이름

# 클래스 변수 읽는 법
# 1. 클래스 이름.클래스 변수 이름
# 2. 인스턴스 이름.클래스 변수 이름
print(User.count)
print(user1.count)
print(user2.count)
print(user3.count)




print("-" * 30)




# 데코레이터

def print_hello():
    print("안녕하세요!")

def add_print_to(original):    # 여기서 add_print_to 함수를 "데코레이터 함수"
    # original = 또 다른 어떤 함수
    def wrapper():
        print("함수 시작")   # original(print_hello)를 꾸며줌 --> "데코레이터"
        original()         # print_hello 함수가 호출됨
        print("함수 끝!")   # original(print_hello)를 꾸며줌 --> "데코레이터"
    return wrapper

add_print_to(print_hello)()  # --> 즉 wrapper()와 같음
# print_hello가 original로 들어감

print_hello = add_print_to(print_hello)
print_hello()


print("-" * 30)




def add_print_to(original):
    def wrapper():
        print("새로운 함수 시작")
        original()
        print("새로운 함수 끝!")
    return wrapper

@add_print_to      # 데코레이터 #print_hello 함수를 add_print_to 함수로 꾸며주라는 뜻
def print_hello():
    print("다시 한번 안녕하세요!")


print_hello()




# 데코레이터는 왜 쓸까?
# 기존의 함수에 새로운 기능을 추가한다

# def function1():
#     기존 함수1 내용

# def function2():
#     기존 함수2 내용

# def function3():
#     기존 함수3 내용


# 모든 함수의 앞 뒤에
# print("이 함수의 시작 부분입니다.") 와
# print("이 함수의 끝 부분입니다.") 를 넣고싶다면



# def add_print_to(original):
#     def wrapper():
#         print("이 함수의 시작 부분입니다.")
#         original()
#         print("이 함수의 끝 부분입니다.")
#     return wrapper

# @add_print_to
# def function1():
#     기존 함수1 내용

# @add_print_to
# def function2():
#     기존 함수2 내용

# @add_print_to
# def function3():
#     기존 함수3 내용



print("-" * 30)



# 인스턴스 메소드: 인스턴스 변수의 값을 읽거나 설정하는 메소드
# 클래스 메소드: 클래스 변수의 값을 읽거나 설정하는 메소드

class User:
    count = 0

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        User.count += 1

    def say_hello(self):
        print("안녕하세요! 저는 {}입니다").format(self.name)

    def __str__(self):
        return "사용자: {}, 이메일: {}, 비밀번호: ****".format(self.name, self.email)

    # 클래스 메소드
    # 첫 번째 파라미터로 클래스를 cls로 전달받는다.
    # 첫 번째 파라미터의 이름은 꼭 "cls"로 쓰기!!!
    @classmethod
    def number_of_users(cls):    # 즉 여기서의 cls는 User 클래스를 나타냄(cls.count == User.count)
        print("총 유저 수는: {} 입니다".format(cls.count))

    # 인스턴스 메소드로도 작성 가능!
    def number_of_users_instance(self):
        print("총 유저 수는: {} 입니다".format(User.count))


user1 = User("비누", "soap@sopa.com", "1234")
user2 = User("꽃", "flower@sss.com", "2345")
user3 = User("핸드폰", "phone@ddd.com", "4567")

# 클래스 메소드
User.number_of_users()
user1.number_of_users()

# 인스턴스 메소드 로도 표현 가능
User.number_of_users_instance(user1)
user1.number_of_users_instance()

# 그렇다면 왜 클래스 메소드로 만든걸까??
# number_of_users_instance 가 인스턴스 변수를 사용하지 않기 때문. --> 파라미터엔 self가 들어가지만 메소드 내용에선 사용 안함

# 따라서 인스턴스 변수를 사용하면 ---> 인스턴스 메소드
# 클래스 변수를 사용하면 ---> 클래스 메소드
# 클래스 변수, 인스턴스 변수 둘 다 쓴다면 인스턴스 메소드를 사용한다 -> 인스턴스 변수, 클래스 변수 모두 사용 가능하기 때문에



# 인스턴스 메소드 vs 클래스 메소드

# 인스턴스 메소드의 사용
# User.say_hello(user1)
# user.say_hello()      --> 인스턴스 자신이 첫번째 파라미터로 자동 전달!

# 클래스 메소드의 사용
# User.number_of_users()
# user1.number_of_users()
# 두 개 모두 다    --> 클래스가 첫번째 파라미터로 자동 전달!
# 두 개 모두 다 파라미터를 빈 것으로 둠. 왜?? class메소드 데코레이터를 사용해 class 메소드로 만들어줬기 때문.



print("-" * 30)



# 인스턴스가 없을 때 필요한 정보가 있다면 --> 클래스 메소드를 사용한다.

class User:
    count = 0

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        User.count += 1

    @classmethod
    def number_of_users(cls):
        print("총 유저 수는: {} 입니다".format(cls.count))


User.number_of_users()
