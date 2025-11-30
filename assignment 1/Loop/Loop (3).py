#3. Number Reverser
num = int(input("Enter an integer: "))
revNum = 0

while num !=0:
  lastNum =num%10
  revNum = revNum*10+lastNum
  num //=10
print(revNum)