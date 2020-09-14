# 지금까지는 변수에 값을 1개씩만 저장했음
my_sum = 7
my_str = "Hello!"
my_bool = True


# [리스트(list)]
# 값을 여러개 저장하고 싶을 때 사용
# 리스트에 담긴 각각의 "요소(element)"들
numbers = [2, 3, 5, 7, 11, 13]  # 숫자형만 담긴 리스트
names = ["소희", "수영", "태린", "영희"]  # 문자열만 담긴 리스트

print(numbers)
print(names)


# [인덱싱(indexing)]
# 인덱스를 통해 요소를 받아옴
# 리스트 안에 있는 요소들을 하나씩 꺼낼 때
# 인덱스: 리스트 안에서 요소의 위치

# 1) 방법
# 리스트이름[인덱스]
print(names[0])
# print(numbers[6])  -> 에러남(5까지만 있으므로)
print(numbers[1] + numbers[3])

num_1 = numbers[1]
num_3 = numbers[3]
print(num_1 + num_3)

# 2) - 인덱스 값
print(numbers[-1])  # 13
print(numbers[-2])  # 11
print(numbers[-6])  # 2
# print(numbers[-7])  -> 에러남(-6까지만 있으므로)

# 3) 리스트에 있는 요소를 변경
# 7을 numbers의 0번 인덱스에 넣어줌
numbers[0] = 7
print(numbers)

numbers[0] = numbers[0] + numbers[1]
# 지정연산자: 오른쪽부터 본다. 7 + 3 = 10 -> 10 대입
print(numbers)


# [리스트 슬라이싱(list slicing)]
# 리스트로 출력

# 방법
# 리스트이름[뽑아내고 싶은 첫 요소 인덱스:뽑아내고 싶은 마지막 요소 인덱스+1]
# 첫 요소 인덱스, 마지막 요소 인덱스+1 -> 둘 중 하나는 생략 가능
print(numbers[0:4])  # numbers 리스트의 0부터 3까지
print(numbers[2:])
print(numbers[:3])

new_list = numbers[:3]  # [2, 3, 5]
print(new_list[2])  # 5




# 리스트에서 사용 가능한 함수

# 1. length
# len(list이름)
# list안의 element 갯수를 세줌
numbers = []
print(len(numbers))

# 2. append(추가 연산)
# list이름.append(추가하고 싶은 값)
# list에 element를 추가하고 싶을 때
# list에서 가장 오른쪽 끝에 들어감
numbers.append(5)
numbers.append(8)
print(numbers)
print(len(numbers))

# 3. delete
# del list이름[삭제하고 싶은 element의 인덱스]
# list에서 element를 삭제하고 싶을 때
numbers = [2, 3, 5, 7, 11, 13, 17, 10]
del numbers[3]
print(numbers)

# 4. insert(삽입 연산)
# list이름.insert(위치인덱스, 넣고싶은 값)
# list의 원하는 위치에 element를 추가할 때
# 원래 값들은 오른쪽으로 한 칸씩 밀려남
numbers = [2, 3, 5, 7, 11, 13, 17, 10]
numbers.insert(4, 37)
print(numbers)





# 리스트 정렬

# 1. sorted 함수
# sorted(리스트이름)   (작은 값부터 올림차순)
# sorted(리스트이름, revers=True)  (큰 값부터 내림차순)
# 기존의 리스트를 건들이지 않고, 새로운 리스트를 만들어 return
numbers = [19, 13, 2, 5, 3, 11, 7, 17]
new_list = sorted(numbers)
print(new_list)

new_list = sorted(numbers, reverse=True)
print(new_list)
print(numbers)


# 2. sort
# 리스트이름.sort()  (작은 값부터 올림차순)
# 리스트이름.sort(reverse=True)  (큰 값부터 내림차순)
# 아무것도 리턴하지 않고, 기존의 리스트를 정렬함

numbers = [19, 13, 2, 5, 3, 11, 7, 17]
print(numbers.sort())
# None. 아무것도 리턴하지 않음. 그냥 numbers를 정렬할 뿐.

numbers.sort()
print(numbers)
# 정렬된 리스트가 나옴

numbers.sort(reverse=True)
print(numbers)




# 리스트에서 값의 존재 확인하기
# 어떤 값이 리스트에 있는지 확인하는 함수를 써보겠습니다

# value가 some_list의 요소인지 확인
def in_list(some_list, value):
    i = 0
    while i < len(some_list):
        # some_list에서 value를 찾으면 True를 리턴
        if some_list[i] == value:
            return True
        i = i + 1
    # 만약 some_list에서 value를 발견하지 못했으면 False를 리턴
    return False

# 테스트
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(in_list(primes, 7))  # True
print(in_list(primes, 12))  # False




# 쓰는데 아주 어렵지는 않습니다.
# 하지만 리스트에 값의 존재를 확인하는 것은 너무 자주 있는 일이라서
# 파이썬에 이미 이 기능이 내장되어 있습니다.
# in이라는 키워드를 쓰면 됩니다.

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(7 in primes)
print(12 in primes)

# 거꾸로 값이 없는지 확인하려면 in 앞에 not을 붙이면 됩니다.
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(7 not in primes)
print(12 not in primes)





# 리스트 안의 리스트 (Nested List)
# 리스트 안에는 또 다른 리스트가 있을 수 있습니다. 이를 영어로 nested list라고 부릅니다.
# 세 번의 시험을 보는 수업
grades = [[62, 75, 77], [78, 81, 86], [85, 91, 89]]

# 첫 번째 학생의 성적
print(grades[0])

# 세 번째 학생의 성적
print(grades[2])

# 첫 번째 학생의 첫 번째 시험 성적
print(grades[0][0])

# 세 번째 학생의 두 번째 시험 성적
print(grades[2][1])

# 첫 번째 시험의 평균
print((grades[0][0] + grades[1][0] + grades[2][0]) / 3)






# 1. sort 메소드
# 저번에 정렬된 새로운 리스트를 리턴시켜주는 sorted 함수를 보여드렸습니다.
# some_list.sort()는 새로운 리스트를 생성하지 않고 some_list를 정렬된 상태로 바꿔줍니다.
numbers = [5, 3, 7, 1]
numbers.sort()
print(numbers)


# 2. reverse 메소드
# some_list.reverse()는 some_list의 원소들을 뒤집어진 순서로 배치합니다.
numbers = [5, 3, 7, 1]
numbers.reverse()
print(numbers)


# 3. index 메소드
# some_list.index(x)는some_list에서 x의 값을 갖고 있는 원소의 인덱스를 리턴해줍니다.
members = ["영훈", "윤수", "태호", "혜린"]
print(members.index("윤수"))
print(members.index("태호"))


# 4. remove 메소드
# some_list.remove(x)는some_list에서 첫 번째로 x의 값을 갖고 있는 원소를 삭제해줍니다.
fruits = ["딸기", "당근", "파인애플", "수박", "참외", "메론"]
fruits.remove("파인애플")
print(fruits)