#document header start
'''
Python program to get the student details
Author: Anannya Abhi
Date:01-10-2024
Version: 1.0
'''
#document header end
name=input('Enter the student name:')
roll_number=int(input('Enter your roll number:'))
roll_number=roll_number+1
cgpa=float(input("Enter your CGPA:"))
percentage=cgpa*10
print ("Name of the student:",name)
print("Roll No:",roll_number)
print("Percentage:",percentage,"%")
