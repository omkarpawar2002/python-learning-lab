"""
PROJECT 3: PRODUCT INFORMATION SYSTEM

Objective:
Create a basic product information program similar to data
found in an e-commerce application.

Store:
- product_name
- product_code
- product_price
- stock_quantity
- category
- company_name
- maximum_stock_capacity

Requirements:
- Use meaningful variable names.
- Use appropriate constants where needed.
- Use type() to inspect values.
- Follow clean formatting.
- Add useful comments.
- Begin with a module-level documentation string.
- Display all stored information.
"""

print("========================================")
print("===== PRODUCT INFORMATION SYSTEM =======")
print("========================================")

product_name = "Laptop"
product_code = "HP#1234"
product_price = 80000
stock_quantity = 20
category = "Electronics"
company_name = "HP"

# Stock Capacity Can Not Exceed This Limit
MAX_STOCK_CAPACITY = 50

print("Product Name       :", product_name)
print("Product Code       :", product_code)
print("Product Price      :", product_price)
print("Stock Quantity     :", stock_quantity)
print("Category           :", category)
print("Company Name       :", company_name)
print("Max Stock Capacity :", MAX_STOCK_CAPACITY)

print()

print("Product Name Type   :", type(product_name))
print("Product Code Type   :", type(product_code))
print("Product Price Type  :", type(product_price))
print("Stock Quantity Type :", type(stock_quantity))
print("Category Type       :", type(category))
print("Company Name Type   :", type(company_name))
print("Max Stock Capacity  :", type(MAX_STOCK_CAPACITY))

print("========================================")
