#
# JamesD, 2025/10/22
# File: JamesD_Correlation_Analysis.py
# Short description of the task
#

import pandas as pd
from scipy import stats 

# 1. Input

df = pd.read_csv ('Correlation_Analysis_Data.csv')

df.info()

# 2. Process
print(df.isnull().sum())
print(df.isnull().sum().sum())
# control and slash to make smth to hashtag

# correlation, pvalue = stats.pearsonr(df['Marketing_Spend'], 
#                                      df['Sales_Revenue'])


# 3. Output

print('Data loaded successfully!')
print (f'Dataset shape: {df.shape}')

# print (f'Correlation:{correlation:.2f}')
# print (f'P value: {pvalue:.4e}')