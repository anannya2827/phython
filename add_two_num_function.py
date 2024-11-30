'''
Name:Anannya Abhi
Date:30/11/24
Python program to write a function to add two numbers
'''
def add_two_num(num1,num2):
    sum=num1+num2
    return sum
in_num1=float(input("Enter the first number:"))
in_num2=float(input("Enter the second number:"))
result=add_two_num(in_num1,in_num2)
print(f"The sum of is: {result}")