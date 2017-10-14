

from scipy.io import arff
import numpy as np
import pandas as pd





dataset = arff.loadarff('supermarket.arff')
# print(dataset)

df = pd.DataFrame(dataset[0])

print(df.head(100))













