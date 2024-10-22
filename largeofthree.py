'''
Author:Anannya Abhi
Date:22/10/2024
Python program to find largest among three numbers
'''
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
if (num1>num2):
    large=num1
else:
    large=num2
if large>num3:
    print("The largest number is:",large)
else:
    print("The largest number is:",num3)
