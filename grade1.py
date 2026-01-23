#Write a program that takes a 5 subject marks from user. calculate total and Percentage  and prints the grade using the following conditions:


#| Percentage | Grade |
#| ---------- | ----- |
#| 90–100     | A+    |
#| 80–89      | A     |
#| 70–79      | B     |
#| 60–69      | C     |
#| 50–59      | D     |
#| below 50   | Need to improve  |

s1=float(input("enter s1 mark"))
s2=float(input("enter s2 mark"))
s3=float(input("enter s3 mark"))
s4=float(input("enter s4 mark"))
s5=float(input("enter s5 mark"))


total=s1+s2+s3+s4+s5
print(total)
per=total/5
print(per)


if(per<=100 and per>=90):
    print("A+")

elif(per<=89 and per>=80):
    print("A")
elif(per<=79 and per>=70):
    print("B")
elif(per<=69 and per>=60):
    print("C")
elif(per<=59 and per>=50):
    print("D")
else:
    print("need to improve")