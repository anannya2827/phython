'''
Desicion making statements in python
Author: Anannya Abhi
Date:15.10.24
'''
# to determine ticket fare
age=int(input("\nEnter your age:"))
if age<10:
  print("Fare=7")
elif age>=10 and age<60:
  print("Fare=10")
else:
  print("Fare=5")