import random
score = 0
while True:
    room = random.randint(1,3)
    num = int(input("방을 입력하세요: "))
    if room == num:
        print("유령이다!!")
        break
    elif room > 3:
        print("잘못된 범위 입니다")
    else:
        print("유령이 없다")
        score += 1
print("==게임 종료==")
print("점수는 %d 입니다" % score)