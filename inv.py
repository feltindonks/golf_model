import numpy as np
import pandas as pd
import csv
import argparse

file_name = 'rbc_heritage_win_european.csv'
top = 1
df = pd.read_csv(file_name)
#drops ev columns
df = df[df.columns.drop(list(df.filter(regex='_ev')))]
#while loop that converts odds to probabilties
cur_col = 2
num_col = (len(df.columns) - 1)
while cur_col <= num_col:
    df[str(cur_col - 1) + '_inv'] = df.iloc[:,cur_col].pow(-1)
    cur_col += 1
#drop odds columns
# df = df[df.columns.drop(list(df.filter(regex='_odds')))]
#change inf to nan
df.replace([np.inf, -np.inf], np.nan, inplace=True)

df['ave_VF'] = (df['2_inv'] /  df['2_inv'].sum())
print (file_name)
sums  = df.sum(axis = 0, skipna = True, numeric_only = True)
print (sums / top)
print (df)
#print ("inv_df:", df)
