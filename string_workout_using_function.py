'''
Name:Anannya Abhi
Date:30/11/24
Python function tht accepts a string and counts number of upper and lower case
'''
def count_of_upper_and_lower_cases(value):
    upper_count=0
    lower_count=0
    for char in value:
        if char.isupper():
            upper_count+=1
        elif char.islower():
            lower_count+=1
    return upper_count,lower_count
input_string=input("Enter a string:")
value=list(input_string)
upper_count,lower_count=count_of_upper_and_lower_cases(value)
print(f'The count of lower case character is:{lower_count}'
      f'\nand that of upper case character is: {upper_count} ')




