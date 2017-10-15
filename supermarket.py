from scipy.io import arff
import numpy as np
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules




print('Loading raw supermarket basket data ...\n')

# read supermarket arrf file available at 
# http://storm.cis.fordham.edu/~gweiss/data-mining/datasets.html
# .arrf file should be placed inside this folder
dataset = arff.loadarff('supermarket.arff')



# convert to dataframe using pandas
df = pd.DataFrame(dataset[0])
# print(df.head())



# discard the last column ('total')
df = df.iloc[:,0:-1] 
# print(df.head())



# check entry types
print('All possible entries in dataframe are:\n', 
	pd.unique(df.values.ravel()))





print('\nEncoding dataframe to binary values ...\n')
def encode_units(x):  # encoder function for each transaction
    if str(x) == "b'?'":
        return 0
    if str(x) == "b't'":
        return 1



# apply the encoder to the dataframe
df_onehot = df.applymap(encode_units)
# print('Original Transaction table:\n', df_onehot.head())






# find all fequent item sets with minimum support value
#    OBS: support here is computed with respect to a single, or set 
#    items. However, to find a support rule just assemble antescedant, and
# 	 consequent items as a single item set.
fq_itemsets = apriori(df_onehot, min_support=0.3, use_colnames=True)
# print('\nFrequent item sets:\n', 
# 	fq_itemsets.sort_values(by='support', ascending=False).head(100))




# list confidence and lift metrics with respect to the association rules
rules = association_rules(fq_itemsets, metric="lift", min_threshold=1.2)
print('Most significant association rules are:\n',
	rules.sort_values(by=['support','confidence'], ascending=False).head(10))

# Try to maximize lift (lift>1) and keep all other metrics >0.5 to find
# reliable rules!