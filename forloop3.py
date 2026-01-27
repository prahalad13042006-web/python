#7) write a program to figure out whether given number  is armstrong number or not

num = int(input("Enter a number: "))

digits = str(num)
power = len(digits)

sum_of_powers = 0

for d in digits:
    sum_of_powers += int(d) ** power

if sum_of_powers == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is NOT an Armstrong Number")
