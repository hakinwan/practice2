user = input("OPEN THE APP ")

login = input("Enter your login details: ")
LOGIN = "1870"
if login == LOGIN:
 print("Login SUCCESSFUL")
else:
 print("Login FAILED")
 exit()


pin = input("Enter your PIN: ")
PIN = "1010"
if pin == PIN:
 print("Correct PIN")
else:
 print("Wrong PIN")
 exit()


#main = input("Show the main menu") 
pick = input("Select Transfer: ")
if pick == "Transfer":
 print("Transfer Selected")
else:
 print("Invalid selection")
 exit()


reci = (input("Enter account number: "))
account = "8143537110"
if reci == account:
    check = input("Confirm transaction details: ")
    print("Valid recipent ")
else:
  print("Invalid recipent")
  exit()

 
bal = 100000
amount = int(input("Enter the amount: "))
if bal >= amount:
 print("Transfer Successful")
else:
 print("insufficient balance")





























