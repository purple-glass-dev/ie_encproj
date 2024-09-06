#Q1: Write a program to determine if the sum of two numbers is divisible 
# by 7 (using if-else) and divisible by 5 (using a ternary operator)

a=int(input("Enter first number :"))
b=int(input("Enter second number :"))
sum = a+b
#Beginning of the if-else block
if (sum%7 == 0):
    print("Divisible by 7")
else:
    print("Not divisible by 7")
#Using ternary operator
div_5= "Divisible by 5" if sum%5==0 else "Not divisble by 5"
print(div_5)
