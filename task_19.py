#Create a dictionary and calculate the average of all values

marks = {
    "Math": 85,
    "Science": 90,
    "English": 78,
    "Computer": 92,
    "History": 80
}

average = sum(marks.values()) / len(marks)

print("Marks Dictionary:", marks)
print("Average of values:", average)
