# market-basket-analysis

The goal of a basket analysis is to find interesting and relevant association rules among purchased items.

mlxtend library 'apriori' algorithm was used here to quickly find rules that are related with a minimum metric of choice value (eg. lift).

Since the 'lift' metric represents an independence scenario for a certain (A) -> (B) rule when lift is equal to 1, reliable association rules are found by maximizing the lift while other metrics, such as support and confidence, are equally considered significant.


## The data 
Dataset corresponds to real supermarket transactions stored in a .arff file that integrates the Weka project platform (https://www.cs.waikato.ac.nz/ml/weka/) and can be found at:

http://storm.cis.fordham.edu/~gweiss/data-mining/weka-data/supermarket.arff

Unfortunately, it seems that there is little information on the dataset itself: 
http://weka.8497.n7.nabble.com/question-of-using-supermarket-arff-for-academic-research-td2573.html
