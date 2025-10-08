#
# James, 2025/10/08
# File: James_Excel.py
# Short description of the task
#

import pandas as pd

# 1. Input
df = pd.read_excel('Financial_Sample.xlsx')

# 2. Process
sum= df.select_dtypes(include='number').sum()
sums= df.select_dtypes(include='number').sum()

sums['Name'] = 'Total'

df_with_total = pd.concat ([df,pd.DataFrame([sums])], ignore_index=True)

# 3. Output
print(df_with_total)
df_with_total.to_excel('output.xlsx', index=False)