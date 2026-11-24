# GLOBAL VARIABLE
x = "fantastic"
def say_hello():
 print("fantastic")
say_hello()

# LOCAL VARIABLE
def say_hello():
  x = "fantastic"
say_hello()
print("fantastic")
 
 # TO CHANGE GLOBAL VARIABLE INSIDE FUNCTION
name = "Hamdan "
def  show_name():
  global name
  name = name + "Akinwande"
show_name()
print(name)