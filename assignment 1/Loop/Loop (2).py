#Armstrong Number Checker
num = int(input("Enter a number: "))

temp = num
digit_Count = 0

for i in range(20):          
    if temp == 0:
        break
    temp //= 10
    digit_Count += 1


temp = num
sum_of_power = 0


for x in range(digit_Count):
    lastNum = temp % 10
    temp //= 10
    sum_of_power += lastNum ** digit_Count


if sum_of_power == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is NOT an Armstrong number")
