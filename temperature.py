'''
Author:Anannya Abhi
Date:22/10/2024
Python program to convert celsius to fahrenheit and vice versa
'''
temperature=float(input("Enter temperature:"))
degree=input("Is this in (C)elsius or (F)ahrenheit?")
if degree=="C" or degree=="c" or degree=="F" or degree=="f":
  if degree=="C" or degree=="c":
      fahrenheit=((9/5)*temperature)+32
      print(temperature,"Celsius is",fahrenheit,"Fahrenheit." )
  else:
      celsius=(5/9)*(temperature-32)
      print(temperature,"Fahrenheit is",celsius,"Celsius")
else:
    print("Invalid input for celsius or fahrenheit")