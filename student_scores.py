student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}

total = sum(student_scores.values())
avg = round(total / len(student_scores), 2)

student_scores["total"] = total
student_scores["avg"] = avg

print(student_scores)
