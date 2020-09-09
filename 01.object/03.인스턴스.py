
# 객체(인스턴스)는 속성과 행동으로 이루어져 있다.
# 속성을 '인스턴스 변수'(변수)로 나타낸다
# 행동은 '함수'(메소드)로 나타낸다


# 메소드는 3가지 종류가 있다
# 1. 인스턴스 메소드
# 2. 클래스 메소드
# 3. 정적 메소드

# <인스턴스 메소드>
# 인스턴스 변수를 사용하거나, 인스턴스 변수가 값을 설정하는 메소드


class User:
    def say_hello(self):
        print("안녕하세요! 저는 {}입니다!!".format(self.name))
        # 여기서 인스턴스 변수(name)를 사용하므로, 인스턴스 메소드라 한다
        # 인사 메세지 출력 메소드
    def login(self, my_email, my_password):   # 3개의 파라미터를 받음
        # 로그인 메소드
        if (self.email == my_email and self.password == my_password):
            # 파라미터로 받은 메일 주소가 유저 인스턴스의 메일 주소(객체의 속성(인스턴스 변수))와 같은지 확인
            print("로그인 성공, 환영합니다.")
        else:
            print("로그인 실패. 없는 아이디이거나 잘못된 비밀번호입니다.")
    def check_name(self, name):
        # 파라미터로 받는 name이 유저의 이름과 같은지 불린으로 리턴하는 메소드
        return self.name == name


# class User:
#     def say_hello(some_user):
#         print("안녕하세요! 저는 {}입니다!!".format(some_user.name))
#         # 여기서 인스턴스 변수(name)를 사용하므로, 인스턴스 메소드라 한다
#         # 인사 메세지 출력 메소드
#     def login(some_user, my_email, my_password):   # 3개의 파라미터를 받음
#         # 로그인 메소드
#         if (some_user.email == my_email and some_user.password == my_password):
#             # 파라미터로 받은 메일 주소가 유저 인스턴스의 메일 주소와 같은지 확인
#             print("로그인 성공, 환영합니다.")
#         else:
#             print("로그인 실패. 없는 아이디이거나 잘못된 비밀번호입니다.")


# 객체 생성
user1 = User()
user2 = User()
user3 = User()

# 객체의 속성
user1.name = "소희소희"
user2.name = "짱구"
user3.name = "이슬이"

user1.email = "sohheee@sohe.com"
user2.email = "shinzzang@email.com"
user3.email = "isle@email.com"

user1.password = "1234"
user2.password = "5678"
user3.password = "1357"


# 인스턴스 메소드 사용법
# 클래스이름.메소드이름(인스턴스)
# 클래스에서 메소드를 호출
User.say_hello(user1)
User.say_hello(user2)
User.say_hello(user3)


# 또 다른 방법
# 인스턴스에 메소드를 호출  --> 이때는 인스턴스가 파라미터로 들어가게 된다
# user1.say_hello(user1) 이런식으로 불가!!!
# 위에 거론된건 즉 User.say_hello(user1, user1) 과 같다.(파라미터를 2개 받는 꼴)
user1.say_hello()   # --> say_hello(user1) 와 같음


# user1.login(user1, "sohheee@sohe.com", "1234") --> 틀린 예시
user1.login("sohheee@sohe.com", "1234")   # user1이 저절로 첫번째 파라미터로 들어감

# 따라서 인스턴스 메소드를 정의할 때는 항상 첫번째 파라미터로 인스턴스를 받기 위한 파라미터를 써줘야한다.
# 이 페이지에서는 some_user로 그걸 받았으나, 앞으로는 'self'로 써야한다.(주인공)
# 첫 번째 파라미터의 이름은 꼭! self로 쓰기

print(user1.check_name("소희소희"))
print(User.check_name(user1, "소희"))




print("-" * 30)




