'''
Python program to get sum of digits
Author: Anannya Abhi
Date:15.10.24
'''
num=int(input("Enter a number:"))
num1=num
sum=0
while num>0:
    remain=num%10
    sum=remain+sum
    num=num//10
print(sum,"is the sum of digits of",num1)

