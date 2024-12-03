'''
Name:Anannya Abhi
Date:3/12/24
Python program to find factorial of a number using recursion
'''
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("Enter the number:"))
ans=factorial(n)
print(f"The factorial of {n} is: {ans}")