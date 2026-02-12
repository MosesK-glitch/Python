# On the try and except block: You run some codes/statements and if it is successful the try block will get executed other the except block will be excuted when there is an anticipated error.

try:
    number = 100
    if number > 10 :
     print("The number is greater than 10 ",)
except Exception as e:
    print("You have an error on your program: ",e)