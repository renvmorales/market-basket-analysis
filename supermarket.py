from scipy.io import arff
import numpy as np
import pandas as pd




# read supermarket arrf file available at 
# http://storm.cis.fordham.edu/~gweiss/data-mining/datasets.html
# .arrf files are Weka datasets types
dataset = arff.loadarff('supermarket.arff')



# convert to dataframe using pandas
df = pd.DataFrame(dataset[0])


# discard the last column ('total')
df = df.iloc[:,0:-1] 
# print(df.head(10))













