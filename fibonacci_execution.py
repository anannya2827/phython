'''
Name:Anannya Abhi
Date:3/12/24
Python program for fibonacci_number() execution
'''
# for importing a user defined function;both files should be in the same project.
import fibonacci_function as fib # we can shorten the function name by using 'as' and renaming as shown here
limit=int(input("Enter the limit:")) # limit taken from user
print(f"{limit} fibonacci numbers are: {fib.fibonacci_number(limit)}")
