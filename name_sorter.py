names = []

while True:
    name = input("請輸入英文姓名（按下Enter結束）：")
    if name == "":
        break
    names.append(name)

# 依字母遞增排序
names_sorted_asc = sorted(names)

# 依字母遞減排序
names_sorted_desc = sorted(names, reverse=True)

# 依字數多寡遞增排序
names_sorted_length_asc = sorted(names, key=len)

# 依字數多寡遞減排序
names_sorted_length_desc = sorted(names, key=len, reverse=True)

print("依字母遞增排序：", names_sorted_asc)
print("依字母遞減排序：", names_sorted_desc)
print("依字數多寡遞增排序：", names_sorted_length_asc)
print("依字數多寡遞減排序：", names_sorted_length_desc)
