#do operation and display result as per user choice about operation using if elif else statements.

#3) write a program to accept month number from user and display how many days month has. (use logical operator or)
 #   input : 1 output : this month has 31 days 
  #  input : 4 output : this month has 30 days 

month=input("enter the month")


if(month=="january"or month=="march"or month=="may"or month=="july"or month=="august"or month=="october"or month=="december"):
    print("31 days")

elif(month=="april"or month=="june"or month=="september"or month=="november"):
    print("30 days")

elif(month=="february"):
    print("28 or 29 days")
else:
    print("invalide")
