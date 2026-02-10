# Functions with parameters
# Parenthesis-> hey are values that get passed as arguements given to a function inside of a parenthesis.


def greeting(name):
    print(f"{name} How are you? Hope everything is fine.")

greeting("Moses")
greeting("George")
greeting("Naomi")
greeting("Janice")

print("================================")
def message(name):
    print(f"Hello {name}. We shall be having a general meeting on date ...... Please avail yourself.")

message("Moses")
message("George")
message("Naomi")
message("Janice")

# Functions that accepts parameters to add two numbers
print("================================")
def addition(x , y):
    sum = x + y
    print("The sum of the numbers is: ", sum)    

addition(45,65)
addition(78,92)