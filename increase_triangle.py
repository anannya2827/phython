'''
Name:Anannya Abhi
Date:19/11/2024
Python program to print an increasing triangle
'''
row=int(input("Enter number of rows:"))
for i in range(row+1):
    for j in range(i):
        print("*",end=" ")
    print()


for i in range(row,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()