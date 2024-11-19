'''
Name:Anannya Abhi
Date:19/11/2024
Python program  to do different operations in a tuple
'''
fruits=('apple','banana','cherry','date')
print(fruits[0],fruits[-1],fruits[-2])
print(len(fruits))
#concatenation
numbers=(1,78,790)
tuple_eg=fruits+numbers
print(tuple_eg)
#repeatition
repeat_tuple=("hi",)*3
print(repeat_tuple)
#membership operator
print('banana' in fruits)
#slicing
colors=('red','green','blue','yellow','orange')
print(colors[0:3])
print(colors[-2:])
print(colors[1:4])
#Unpack tuple into variable
person=('Alice',25,'Engineering')
name,age,profession=person
print(f"{name}\n{age}\n{profession}")