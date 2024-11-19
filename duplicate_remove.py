'''
Name:Anannya Abhi
Date:19/11/2024
Python program to remove duplicate elements from a list
'''
list=[1,3,44,26,26,44,76,87,91,1,22]
unique_list=[]
for number in list:
    if number not in unique_list:
      unique_list.append(number)
print(f"The list without duplicate value is: {unique_list}")
print(f"The original list is: {list}")

