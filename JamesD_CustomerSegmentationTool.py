#
# JamesD, 2025/10/23
# File: JamesD_CustomerSegmentationTool.py
# Short description of the task
#

import pandas as pd

# 1. Input
df = pd.read_excel('customers.xlsx')

print (df)

# 2. Process
# Tracking Variables
vip_customers = []
regular_customers = []
new_customers = []
total_vip_revenue = 0
customers = vip_customers, regular_customers, new_customers

# Tracking Variables
# total_original = 0
# total_discount = 0
# total_final = 0
# total_product = 0


# def customers(row):
#     if row['Total_Purchases'] > 10000:
#         #category = "VIP"
#         return 'VIP'
#     elif row['Total_Purchases'] >=5000:
#         #category = 'Regular'
#         return 'Regular'
#     else:
#         #category = 'New'
#         return 'New'
    

for customer in customers:
    names = df.loc['Customer_Name']
    purchases = df.loc['Total_Purchases']
    orders = df.loc['Number_of_Orders'] 
    if ['Total_Purchases'] > 10000:
        category = 'VIP'
    elif ['Total Purchases'] >=5000:
        category = 'Regular'
    else:
        category = 'New'

vip_customers = 
    

    





# 3. Output
print (f"CUSTOMER SEGMENTATION REPORT")