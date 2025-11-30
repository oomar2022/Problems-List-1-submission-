#Simple Calculator: Input two numbers and an operator
num1 = int(input("1st Number: "))
num2 = int(input("2nd Number: "))
operator = input("(+, -, *, /): ")

if operator == "+":
    print("Result: ",num1 + num2)

elif operator == "-":
    print("Result: ",num1 - num2)

elif operator == "*":
    print("Result: ",num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("Result: ",num1 / num2)
    else:
        print("Error: Cannot divide by zero!")

else:
    print("Invalid operator!")