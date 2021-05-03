import numpy as np
import pandas as pd
import csv
import argparse

file_name = 'wel_win_3_noon.csv'
mod_file = str('edit_' + str(file_name))
def_top = 1
df = pd.read_csv(file_name)

parser = argparse.ArgumentParser()
parser.add_argument('--top', default=def_top)
args = parser.parse_args()
top = args.top
#drops ev columns
df = df[df.columns.drop(list(df.filter(regex='_ev')))]

#while loop that converts odds to probabilties
cur_col = 2
num_col = (len(df.columns) - 1)
while cur_col <= num_col:
    df[str(df.columns[cur_col])[:5] + '_%'] = df.iloc[:, cur_col].pow(-1)
    cur_col += 1

#drop odds columns
df = df[df.columns.drop(list(df.filter(regex='_odds')))]
#change inf to nan
df.replace([np.inf, -np.inf], np.nan, inplace=True)

sums  = df.sum(axis = 0, skipna = True, numeric_only = True)
print ("top is" + str(top))
print ("sums/top:" + str(sums / int(top)))
print (df.head())
print('find csv @ ' + mod_file)
df.to_csv(mod_file, index=False) #index=False means no index column @ col[0]

#below an example from cheatsheet
#Append a column of row sums to a DataFrame
#df['Total'] = df.sum(axis=1)
