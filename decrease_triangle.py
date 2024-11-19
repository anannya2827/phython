'''
Name:Anannya Abhi
Date:19/11/2024
Python program to print a decreasing triangle
'''
row=int(input("Enter the number of rows:"))
for i in range(row,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()