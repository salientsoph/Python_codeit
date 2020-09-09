
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
