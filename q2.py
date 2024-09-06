#Q2: Write a program to calculate the factorial of a given number using a for loop.

a=int(input("Enter your number :"))
f=1
for i in range(1,a+1,1):
    f*=i
print("Factorial of the number",a,"is:",f)