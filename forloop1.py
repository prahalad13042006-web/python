#write a program to figure out whether given number  is composite number or not
num = int(input("Enter a number: "))

if num <= 1:
    print("Not a composite number")
else:
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count > 2:
        print(num, "is a Composite number")
    else:
        print(num, "is NOT a Composite number")
