'''
Name:Anannya Abhi
Date:3/12/24
Python program to find greatest common divisor using recursion
'''
def gcd(num1,num2):
    if num1%num2==0:
        return num2
    else:
        return gcd(num2,num1%num2)
num1 = int(input(f"Enter the first number:"))
num2 = int(input(f"Enter the second number:"))
ans=gcd(num1,num2)
print(f'The greatest common divisor is: {ans}')