# Fibonacci Sequence
a = 0
b = 1
n = int(input("Enter N: "))
for x in range(n):
     print(a,end=" ")
     c = a + b
     a = b
     b = c