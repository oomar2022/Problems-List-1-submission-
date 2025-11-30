#Quadrant Identifier Python program

x = int(input("Enter x-coordinate: "))
y = int(input("Enter y-coordinate: "))

if x>0 and y>0:
    print("1st Quadrant")
elif x<0 and y>0:
    print("2nd Quadrant")
elif x<0 and y<0:
    print("3rd Quadrant")
else:
    x>0 and y<0
    print("4th Quadrant")