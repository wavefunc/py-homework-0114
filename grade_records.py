records = []
total_score = 0

while True:
    name = input("請輸入姓名：")
    if name == "":
        break
    try:
        grade = float(input("請輸入成績："))
        record = {"name": name, "grade": grade}
        records.append(record)
        total_score += grade
    except ValueError:
        print("輸入的成績不是數字，請重新輸入")

average_score = round(total_score / len(records), 2)

print("總分：", total_score)
print("平均：", average_score)
