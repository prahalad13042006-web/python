amount = int(input("Enter amount in rupees: "))

rupees= [500, 200, 100, 50, 20, 10, 5, 2, 1] 

for c in rupees:
    count = amount // c
    if count > 0:
        value = c * count
        print(f"{c} x {count} = {value:02d}")
        amount = amount % c
