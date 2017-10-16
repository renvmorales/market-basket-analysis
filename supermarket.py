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
# print(df.head(10))

# Raw dataframe has (4627, 217) shape
print('Original dataset size: ', df.shape)
# print('\n')


# discard the last column ('total')
df = df.iloc[:,0:-1] 
# print(df.head())



# check entry types
print('All possible entries in dataframe are:\n', 
	pd.unique(df.values.ravel()))



print('\nEncoding dataframe to binary values ...')
def encode_units(x):  # encoder function for each transaction
    if str(x) == "b'?'":
        return 0
    if str(x) == "b't'":
        return 1



# apply the encoder to the dataframe
df_onehot = df.applymap(encode_units)
# print('Original Transaction table:\n', df_onehot.head())



# some descriptive statistics on the dataset
print('Total different purchased items: ', df_onehot.values.sum())
print('Total number of transactions with at least one purchased item: ', 
	np.sum(df_onehot.values.sum(axis=1)>0, axis=0) )
print('Average number of purchased items per transaction: %.1f' % 
	np.mean(df_onehot.values.sum(axis=1)) )




# find all fequent item sets with minimum support value
#    OBS: support here is computed with respect to a single, or set 
#    items. However, to find a support rule just assemble antescedant, and
# 	 consequent items as a single item set.
fq_itemsets = apriori(df_onehot, min_support=0.3, use_colnames=True)
# print('\nFrequent item sets:\n', 
# 	fq_itemsets.sort_values(by='support', ascending=False).head(100))




# list confidence and lift metrics with respect to the association rules
rules = association_rules(fq_itemsets, metric="lift", min_threshold=1.2)
print('\nMost significant association rules are:\n',
	rules.sort_values(by=['support','confidence'], ascending=False).head(10))

# Try to maximize lift (lift>1) and keep all other metrics >0.5 to find
# reliable rules!