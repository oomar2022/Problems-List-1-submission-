#4. Sum of Digits python program
num = int(input("Enter a integer Number"))
count=0
while num !=0:
      last_Digit = num%10
      num//=10
      count=count+last_Digit
print(count)

