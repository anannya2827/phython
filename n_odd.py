'''
Program to generate n odd numbers in python
Author: Anannya Abhi
Date:15.10.24
'''
limit=int(input("Enter a limit:"))
odd_num=1
count=0
while count<limit:
   print(odd_num,"\t",end="")
   odd_num+=2
   count+=1
