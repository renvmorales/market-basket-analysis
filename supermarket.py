from scipy.io import arff
import numpy as np
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules




# read supermarket arrf file available at 
# http://storm.cis.fordham.edu/~gweiss/data-mining/datasets.html
# .arrf files are Weka datasets types
dataset = arff.loadarff('supermarket.arff')



# convert to dataframe using pandas
df = pd.DataFrame(dataset[0])


# discard the last column ('total')
df = df.iloc[:,0:-1] 
# print(df.head())




# create a encoder function for each transaction
def encode_units(x):
    if str(x) == "b'?'":
        return 0
    if str(x) == "b't'":
        return 1




# apply the encoder to the dataframe
df_onehot = df.applymap(encode_units)
print('Original Transaction table:\n')
print(df_onehot.head())







