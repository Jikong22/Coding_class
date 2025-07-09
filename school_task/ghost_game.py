import random
score = 0
while True:
    room = random.randint(1,3)
    num = int(input("방 번호를를 입력하세요: "))
    if room == num:
        print("유령이다!!")
        break
    elif num > 3:
        print("%d번 방은 없습니다"%num)
    else:
        print("유령이 없다!")
        score += 1
print("==게임 종료==")
print("점수 : %d" % score)