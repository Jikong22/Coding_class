N = int(input("정수를 입력하세요 (1 이상 20 이하): "))

if 1 <= N <= 20:
    for i in range(1, N + 1):
        print("*" * i)
else:
    print("1 이상 20 이하의 자연수를 입력해야 합니다.")
