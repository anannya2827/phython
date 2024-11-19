'''
Name:Anannya Abhi
Date:19/11/2024
Python program to print hill pattern
'''
limit=int(input("Enter the limit:"))
for i in range(1,limit+1):  #for rows
    for j in range(limit-i):  # for space (depends on limit)
        print(" ",end=" ")
    for k in range(2*i-1): #for star
        print("*",end=" ")
    print()

