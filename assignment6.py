#3. a function that accepts a number(uses input function), checks whether the number is positive,negative or zero and prints the result, using,if,elif,else.
def check_number():

    num=int(input("Enter a number: "))
    if num>0:
        print("The number is positive")
    elif num<0:
        print("The number is negative.")
    else:
        print("The number is neutral.")

check_number() # invoking the function
print("===========================")

#4. a function that accepts the number n, uses a for loop and claculates the sum of numbers from 1 to n
def sum_of_numbers(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    print("The sum of numbeers from 1 to",n,"is:",sum)
n=int(input("Enter a number: "))
sum_of_numbers(n)
print("====================================")

#5. a function that accepts a number, uses a while loop and calculates the square of numbers from 1 to that number.
def square_of_numbers(n):
    i=1
    while i<=n:
        square=1**2
        print("The square of",i, "is:",square)
        i=+1
n= int(input("Enter a number: "))
square_of_numbers(n)
