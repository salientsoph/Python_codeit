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

# 방법
# 리스트이름[인덱스]
print(names[0])
# print(numbers[6])  -> 에러남(5까지만 있으므로)
print(numbers[1] + numbers[3])

num_1 = numbers[1]
num_3 = numbers[3]
print(num_1 + num_3)

# - 인덱스 값
print(numbers[-1])  # 13
print(numbers[-2])  # 11
print(numbers[-6])  # 2
# print(numbers[-7])  -> 에러남(-6까지만 있으므로)

# 리스트에 있는 요소를 변경
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




