#7. Password Retry System 
predefined_password = "omar123"
attemp = 0
while attemp < 3:
  password = input("Enter password: ")
  
  if password == predefined_password:
    print("Successfully Login")
    break
  
  else:
    print("Please Enter Correct Password")

  attemp = attemp + 1

if attemp == 3 and password != predefined_password:
  print("Account locked,Too many wrong attempts")