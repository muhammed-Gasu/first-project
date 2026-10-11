marks = [5, 4, 3, 4, 5, 5, 3]

lowest = marks[0]
highest = marks[0]
sum_marks = 0

for m in marks:
    if m < lowest:
        lowest = m
    if m > highest:
        highest = m
    sum_marks += m

mean_score = sum_marks / len(marks)

print("Самая низкая оценка:", lowest)
print("Самая высокая оценка:", highest)
print("Среднее арифметическое:", mean_score)
