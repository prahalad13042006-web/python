#Create a dictionary of 5 students with their marks and find the total marks.

students = {
    "Rahul": 85,
    "Mohan": 78,
    "Manan": 92,
    "Darshan": 88,
    "Prahlad": 90
}

total_marks = sum(students.values())

print("Students and their marks:")
for name, marks in students.items():
    print(name, ":", marks)

print("Total marks:", total_marks)
