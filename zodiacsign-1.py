#4) write a program to accept birth day and birth month from user as separate input. decide zodiac sign from below table 
    


    #Aries: March 21–April 19
    #Taurus: April 20–May 20
    #Gemini: May 21–June 21
    #Cancer: June 22–July 22
    #Leo: July 23–August 22
    #Virgo: August 23–September 22
    #Libra: September 23–October 22
    #Scorpio: October 24–November 21
    #Sagittarius: November 22–December 21
    #Capricorn: December 22–January 19
    #Aquarius: January 20–February 18
    #Pisces: February 19–March 20

day = int(input("Enter your birth day: "))
month = input("Enter your birth month: ").lower()


if (month == "march" and day >= 21) or (month == "april" and day <= 19):
    sign = "Aries"
elif (month == "april" and day >= 20) or (month == "may" and day <= 20):
    sign = "Taurus"
elif (month == "may" and day >= 21) or (month == "june" and day <= 21):
    sign = "Gemini"
elif (month == "june" and day >= 22) or (month == "july" and day <= 22):
    sign = "Cancer"
elif (month == "july" and day >= 23) or (month == "august" and day <= 22):
    sign = "Leo"
elif (month == "august" and day >= 23) or (month == "september" and day <= 22):
    sign = "Virgo"
elif (month == "september" and day >= 23) or (month == "october" and day <= 22):
    sign = "Libra"
elif (month == "october" and day >= 23) or (month == "november" and day <= 21):
    sign = "Scorpio"
elif (month == "november" and day >= 22) or (month == "december" and day <= 21):
    sign = "Sagittarius"
elif (month == "december" and day >= 22) or (month == "january" and day <= 19):
    sign = "Capricorn"
elif (month == "january" and day >= 20) or (month == "february" and day <= 18):
    sign = "Aquarius"
elif (month == "february" and day >= 19) or (month == "march" and day <= 20):
    sign = "Pisces"
else:
    sign = "Invalid date"

print("Your Zodiac Sign is:", sign)
2
