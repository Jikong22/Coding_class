dan=1
while dan!=0:
     dan=int(input("구구단 몇단을 계산할가요?(1~9)"))
     if dan==0:
          print("구구단 게임을 종료합니다.")
     else:
          print("구구단 %s단을 계산합니다"%dan)
     number=0
     while number<=8 and dan!=0:
          number=number+1
          print("%d x %d = %d" %(dan,number,dan*number))
