'''
Name:Anannya Abhi
Date:29/10/2024
Python program to print multiplication of a number till 12
'''
number=int(input("Enter a number:"))
print(f"Multiplication of {number} till 12 is:")
for i in range(13):
  product=i*number
  print(f"\n {i}*{number}\t=\t{product}")

