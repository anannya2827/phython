'''
Name:Anannya Abhi
Date:19/11/2024
Python program  to do different operations in a list'''
l1_elements=int(input("Enter the number of elements in First list:"))
list1=[]
list2=[]
for i in range(0,l1_elements):
  num=int(input("Enter the element:"))
  list1.append(num)
l2_elements=int(input("Enter the size of second list: "))
for i in range(0,l2_elements):
    num1=int(input("Enter the element:"))
    list2.append(num1)
combined_list=list1+list2
print(combined_list)
even_list=[]
odd_list=[]
for i in list1:
    if i % 2 == 0:                                        # OR even_list=[number for number in combined_list if number%2==0
        even_list.append(i)                               # OR odd_list=[number for number in combined_list if number%2!=0 ?
    else:
        odd_list.append(i)
print(even_list,odd_list)
even_list.sort()
odd_list.sort()
print(even_list,odd_list)
merged_list=even_list+odd_list
print(merged_list)
