#
# JamesD, 2025/10/16
# File: JamesD_MiniProject.py
# Short description of the task
#

# 1. Input

products = [ 
{"name": "Laptop", "price": 1200, "category": "Electronics"}, 
{"name": "Shirt", "price": 45, "category": "Clothing"}, 
{"name": "Phone", "price": 800, "category": "Electronics"}, 
{"name": "Shoes", "price": 120, "category": "Clothing"}, 
{"name": "Tablet", "price": 350, "category": "Electronics"}, 
{"name": "Jacket", "price": 95, "category": "Clothing"}, 
{"name": "Book", "price": 25, "category": "Books"}, 
{"name": "Headphones", "price": 150, "category": "Electronics"}
] 

# 2. Process
def calculate_discount(price, category):
	if category == "Electronics" : 
		if price >= int(1000):
			discount = int(0.20)
		elif price >= int(500):
			discount = int(0.15)
		else:
			discount = int(0.10)
	if category == "Clothing":
		if price >= int(100):
			discount = int(0.25)
		else:
			discount = int(0.10)
	if category == "Books":
		discount = int(0.10)
	return discount, price

Total_Original = 0
Total_Discount = 0
Total_Final = 0


# 3. Output
print ("\n===PRODUCT DISCOUNT CALCULATOR===")

for product in products:
	product = ["name"]
	Category = ["category"]
	Original_Price = ["price"]
	Discount = calculate_discount