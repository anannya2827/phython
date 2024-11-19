'''
Name:Anannya Abhi
Date:19/11/2024
Python program for inventory management system for a store
'''
inventory=[
    ("Laptop",8,30000.00),
    ("Headphones",15,500.00),
    ("Mouse",50,150.00),
    ("Monitor",10,3000.00)
]
highest_stock_value=0
item_with_highest_stock_value=None
for item in inventory:
    item_name,quantity,unit_price=item
    total=quantity*unit_price
    print(f"Total stock value of {item_name} is: {total}")
    if total>highest_stock_value:
      highest_stock_value=total
      item_with_highest_stock_value=item_name
print(f"Item with highest stock value is:{item_with_highest_stock_value}")
print(f"The highest stock value is:{highest_stock_value}")

