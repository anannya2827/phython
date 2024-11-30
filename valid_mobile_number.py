'''
Name:Anannya Abhi
Date:30/11/24
Python program to check whether the given mobile number is valid or not
'''
def valid_mobile_number():
 mobile_num = input("Enter the mobile number:")
 if len(mobile_num)!=10:
    print("The given mobile number is INVALID!(not a ten digit number)")
 else:
    if mobile_num[0] in "7,8,9":
        print("The given mobile number is VALID!")
    else:
        print("The given mobile number is INVALID!(number should start with 7 or 8 or 9)")
valid_mobile_number()