# 1. while 반복문
# 무언가를 반복하기 위해 사용

# [while 반복문 구조]
# while 조건 부분:
#   수행 부분

# 명제가 True면 수행부분 실행, False면 반복문 종료
# 조건 부분: 그 명령들을 실행하기 위한 조건(불린값으로 계산되는 식)(명제)
# 수행 부분: 반복적으로 실행하고 싶은 명령

# ex)
# 사이트에 있는 모든 이미지를 다 다운로드 받으면, 이 반복문을 끝낸다!
# while 다운로드 안 받은 이미지가 있다:
#   다음 이미지를 보고, 다운로드 받는다


# 3번 반복
i = 1
while i <= 3:
    print("파이썬 잘 배우자!")
    i += 1



# 2. if 문
# 만약(if), 그렇지 않으면(else)

# [if문 구조]
# if 조건 부분:
#   수행 부분1
# [else:
#   수행 부분2]

# 조건 부분: 불린값으로 계산되는 식(명제)
# 수행 부분1: 조건을 충족했을 때, 실행하고 싶은 명령


# ex)
# while 다운로드 안 받은 이미지가 있다:
#   다음 이미지를 본다
#   if 이미지가 png 파일이다:
#       이미지를 다운로드 받는다
#   else:
#       print("png가 아니네요!")


temperature = 8
if temperature <= 10:
    print("자켓 입으세요!")
else:
    print("자켓 안 입어도 돼요!")

# 경우의 수가 많을 때1
temperature2 = 5
if temperature2 <= 10:
    print("자켓을 입는다")
else:
    if temperature2 <= 15:
        print("긴팔을 입는다")
    else:
        print("반발을 입는다")

# 경우의 수가 많을 때2
score = 90
if score >= 90:
    print("A")
else:
    if score >= 80:
        print("B")
    else:
        if score >= 70:
            print("C")
        else:
            if score >= 60:
                print("D")
            else:
                print("F")

# else와 if 문이 중첩됨 -> elif문 사용



# 3. elif 문
# 수행부분이 여러개지만, 조건에 맞는 단 1개의 수행부분만 실행된다

score = 74
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")




# 4. break문
# 만약 while문의 조건 부분과 상관 없이 반복문에서 나오고 싶으면, break문을 사용하면 됩니다.

i = 100
while True:
    # i가 23의 배수면 반복문을 끝냄
    if i % 23 == 0:
        break
    i = i + 1
print(i)



# 5. continue문
# 현재 진행되고 있는 수행 부분을 중단하고 바로 조건 부분을 확인하고 싶으면 continue문을 쓰면 됩니다.

i = 0
while i < 15:
    i = i + 1
    # i가 홀수면 print(i) 안 하고 바로 조건 부분으로 돌아감
    if i % 2 == 1:
        continue
    print(i)