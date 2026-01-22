#4)   0    1   1   2   3   5   8   13  .... 100


a = 0
b = 1

print(a, b, end=" ")

while b <= 100:
    c = a + b
    if c > 100:
        break
    print(c, end=" ")
    a = b
    b = c
