# Boolean- This data type represents one of two values: True or False.
is_sunny = True
is_raining = False
print(is_sunny)  # Output: True
print(is_raining)  # Output: False

paidloan = True
print(paidloan)  # Output: True
print(type(paidloan))  # Output: <class 'bool'>

# comparison operators: they are used to compare two values and return a boolean result (True or False).
number1 = 10
number2 = 20 
print("Is number1 greater than number2?", number1 > number2) 
print("Is number1 less than number2?", number1 < number2) 
print("Is number1 equal to number2?", number1 == number2)
print("Is number1 not equal to number2?", number1 != number2)
print("Is number1 greater than or equal to number2?", number1 >= number2)
print("Is number1 less than or equal to number2?", number1 <= number2)

# Logical operators: they are used to combine multiple boolean expressions and return a boolean result.
# logical and
# it returns True if both expressions are True, otherwise it returns False.
print((3>1) and (7>6))  # Output: True

# logical or
# it returns True if at least one of the expressions is True, otherwise it returns False.
print((3>1) or (7<6))  # Output: True
# logical not
# it returns the opposite of the boolean value. If the expression is True, it returns False, and if the expression is False, it returns True.
print(not (3>1))  # Output: False