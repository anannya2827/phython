'''
Name:Anannya Abhi
Date:3/12/24
Python program to add 2 numbers using recursion
'''
def add_two_numbers(num1,num2):
    if num2==0:
        return num1
    else:
        return add_two_numbers(num1+1,num2-1)
num1 = int(input(f"Enter the first number:"))
num2 = int(input(f"Enter the second number:"))
sum=add_two_numbers(num1,num2)
print(f"The sum is: {sum}")