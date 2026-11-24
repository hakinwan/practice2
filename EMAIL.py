#Receive the user's email and password.
#Look up the stored password for that email.
#If the email is not found, return "Account does not exist."
#Compare the entered password with the stored password.
#If the passwords match, return "Login successful."
#If the passwords do not match, return "Incorrect password."






email = "hamdalah710@gmail.com"
password = "ham@1111"

user = input("Enter your email: ")
if user != email:
    print("Incorrect email ")
    exit()

pas = input("Enter your password: ")

if user != email:
    print("Account does not exist")

elif pas == password:
    print("Login successful")

else:
    print("Incorrect password")



#email = "hamdalah@gmail.com"
#password = "ham@1111"

#user = input("Enter your email: ")
#pas = input("Enter your password: ")

#if user != email:
 #   print("Account does not exist")
#elif pas == password:
 #   print("Login successful")
#else:
 #   print("Incorrect password")