import random
num = random.randint(1, 20)
count = 0
while True:
  count += 1
  print("%d번째 시도입니다!"%count)
  my_guess = int(input("1~20 사이의 숫자를 입력하세요:"))
  if my_guess < 1 or my_guess > 20:
    print("잘못된 범위 입니다")
  elif num == my_guess:
    print("정답입니다!")
    print("%d번 만에 정답을 맞췄습니다"%count)
    break
  elif num > my_guess:
    print("업")
  else:
    print("다운")