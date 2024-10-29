'''
Name:Anannya Abhi
Date:29/10/2024
Python program to count number of vowels and consonants in a string
'''
input_string=input("Enter a string:")
vowels="AEOIUaeiou"
vowel_count=0
consonant_count=0
for char in input_string:
    if char in vowels: #used membership operator
        vowel_count+=1
    else:
        consonant_count+=1
print(f"The number of vowels in {input_string} is:{vowel_count}")
print(f"The number of consonants in {input_string} is:{consonant_count}")
