'''
Name:Anannya Abhi
Date:3/12/24
Python program to find multiplication of 2 numbers using recursion
'''
def multiply(num1,num2):
    if num2==1:
        return num1
    else:
        return num1+multiply(num1,num2-1)
num1=int(input(f"Enter the first number:"))
num2=int(input(f"Enter the second number:"))
result=multiply(num1,num2)
print(f"The product of {num1}*{num2} is: {result}")
