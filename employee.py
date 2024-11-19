'''
Name:Anannya Abhi
Date:19/11/2024
Python program for employee management system
'''
list=[
    ('Arun','HR',15000.00),
    ("Leo",'IT',30000.00),
    ('Daisy','Technical Analyst',45000.00),
    ('Lily',"HR",20000.00),
]
payroll=0
annual_payroll=0
for employee in list:
    name,department,salary=employee
    if salary>25000:
        print(f"{name} has salary above 25000.It is {salary}")
    payroll=payroll+salary
    annual_payroll=12*payroll
print(f"The total annual payroll is: {annual_payroll}")