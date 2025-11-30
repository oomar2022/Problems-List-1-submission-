#1. Largest among Three Numbers Python program

num1 = int(input("1st Number:"))
num2 = int(input("2nd Number:"))
num3 = int(input("3rd Number:"))

if num1>num2 and num1>num3:
    print("Largest Number is:",num1)
elif num2>num1 and num2>num3:
    print("Largest Number is:",num2)
else:
    print("Largest Number is:",num3)

