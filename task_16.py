#Given a tuple of numbers, convert it into a list and add new elements.

numbers_tuple = (10, 20, 30, 40)

numbers_list = list(numbers_tuple)

numbers_list.append(50)
numbers_list.append(60)

print("Original tuple:", numbers_tuple)
print("Converted list:", numbers_list)
