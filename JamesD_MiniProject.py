#
# JamesD, 2025/10/16
# File: JamesD_MiniProject.py
# Short description of the task
#

# 1. Input

products = [{"name": "Laptop", "price": 1200, "category": "Electronics"},{"name": "Shirt", "price": 45, "category": "Clothing"},
			{"name": "Phone", "price": 800, "category": "Electronics"},{"name": "Shoes", "price": 120, "category": "Clothing"},
			{"name": "Tablet", "price": 350, "category": "Electronics"},{"name": "Jacket", "price": 95, "category": "Clothing"},
			{"name": "Book", "price": 25, "category": "Books"},{"name": "Headphones", "price": 150, "category": "Electronics"}]


# 2. Process

# Initialize Tracking Variables
total_original = 0
total_discount = 0
total_final = 0
total_product = 0

print ("=== PRODUCT DISCOUNT CALCULATOR ===\n")

# Process Each Product
for product in products:
	name =  product["name"]
	price = product["price"]
	category = product["category"]
	total_product += 1
	
# Discount Rate
if category == "Electronics":
	if price >= 1000:
		discount = 0.2
	elif price >= 500:
		discount = 0.15
	else:
		discount = 0.1
elif category == "Clothing":
	if price >= 100:
		discount = 0.25
	else: 
		discount = 0.15
elif category == "Books":
	discount = 0.1
else:
	discount = 0

# Discount Calculation
discount_percent = discount * 100
discount_price = price * discount
final_price = price - discount_price

# New Product Variables
total_original += price
total_discount += discount_price
total_final += final_price

# 3. Output

# Product Details
print(f"\nProduct: {name}")
print(f"\nCategory: {category}")
print (f"\nOriginal Price: ${price}")
print (f"\nDiscount: {discount_percent}%")
print (f"\nFinal Price: ${final_price}")

# Summary Report
print("=== SUMMARY ===")
print(f"\nTotal Products: {total_product}")
print(f"\nTotal Original Price: ${total_original}")
print(f"\nTotal Discount: ${total_discount}")
print(f"\nTotal Final Price: ${total_final}")