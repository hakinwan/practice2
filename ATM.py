user = input("insert your card")
correct_pin = "1927"
pin = input("what is your pin ? ")
if pin == "1927":
    print("proceed") 
else:
    print("incorrect pin")
    print("reject")
amount = int(input("enter the amount: "))  
bal = 10000
if amount < bal:
    print("withdraw")
else:
    print("insufficient bal")

