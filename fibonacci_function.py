'''
Name:Anannya Abhi
Date:3/12/24
Python program for fibonacci_number()
'''
def fibonacci_number(n):
    sequence=[]
    first_number,second_number=0,1 # initializing in a single statement
    for _ in range(n):
        sequence.append(first_number)
        first_number,second_number=second_number,first_number+second_number
    return sequence