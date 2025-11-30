#Age Classifier Python program

age = int(input("Enter Your Age:"))

if age>0 and age<=1:
    print("infant")
elif age>=2 and age<=3:
    print("toddler")
elif age>=4 and age<=12:
    print("Child")
elif age>=13 and age<=19:
    print("teenager")
elif age>=20:
    print("Adult")
else:
    print("Invalid Age!")
