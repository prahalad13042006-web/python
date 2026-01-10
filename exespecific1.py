#Count how many times a specific value appears in a list using built-in methods.



numbers = [10, 20, 30, 20, 40, 20, 50]

value = int(input("Enter the value to count: "))

count = numbers.count(value)

print("List:", numbers)
print(f"{value} appears {count} times in the list")
