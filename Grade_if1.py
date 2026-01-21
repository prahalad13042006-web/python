
marks = []
for i in range(1, 6):
    m = float(input(f"Enter marks for subject {i}: "))
    marks.append(m)

total = sum(marks)
percentage = total / 5


if 90 <= and<= 100:
    grade = "A+"
elif 80 <= and <= 89:
    grade = "A"
elif 70 <= and <= 79:
    grade = "B"
elif 60 <= and <= 69:
    grade = "C"
elif 50 <= and <= 59:
    grade = "D"
else:
    grade = "Need to improve"


print("\nTotal Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
