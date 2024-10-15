'''
Sequence statements in python
Author: Anannya Abhi
Date:15.10.24
'''
#smallest of three numbers
num1 = int(input("\nEnter a first number:"))
num2 = int(input("Enter a second number:"))
num3 = int(input("Enter a third number:"))
if num1<num2:
    if num1<num3:
        print(num1,"is smallest")
    else:
        print(num3,"is smallest")
elif num2<num3:
    print(num2,"is smallest")
elif num3<num1:
    print(num3,"is smallest")
else:
     print("Numbers are equal")

