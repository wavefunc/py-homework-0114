n = int(input("請輸入星星數："))

# 確保輸入的數字是奇數
if n % 2 == 0:
    print("請輸入奇數！")
else:
    # 上半部分
    for i in range(n // 2 + 1):
        print(" " * (n // 2 - i) + "*" * (2 * i + 1))

    # 下半部分
    for i in range(n // 2):
        print(" " * (i + 1) + "*" * (n - 2 * (i + 1)))
