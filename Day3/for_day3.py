n = int(input("정수를 입력하시오:"))
result = 1
for i in range(1, n+1, 1):
    result = result*i
print("%d!은 %d입니다."%(n, result))