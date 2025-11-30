# Guess the Number Game
import random
jackpot = random.randint(1,10)

count = 0
while count<3:
    gussNumber = int(input("Guess Number is:"))
    count=count+1
    if jackpot == gussNumber:
     print("Congratulations!You Won!")
     break
    elif jackpot > gussNumber:
      print("Too low! Try again.")
    elif jackpot< gussNumber:
      print("Too high! Try again.")

if count == 3 and gussNumber != jackpot:
    print("You Lose! The correct number was:", jackpot)
   

    
