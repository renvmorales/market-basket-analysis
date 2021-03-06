# market-basket-analysis

The goal of a basket analysis is to find interesting and relevant association rules among purchased items.

mlxtend library 'apriori' algorithm was used here to localize most frequent items, e.g., the ones that satisfies a minimum support value criterion.

Next, frequent items are aggregated and submitted to a lift evaluation in order to find candidates of 'good' rules. Since a lift value equals to 1 indicates an independence scenario for a certain (A) -> (B), reliable association rules are found by maximizing this metric. However, it is equally important to check whether other metrics, such as support and confidence, reach a desired tolerance like 50 %.



## About the data 
The dataset corresponds to a real supermarket transactional table (4627 rows and 217 columns) stored in a .arff format. The raw dataset file integrates the Weka project (https://www.cs.waikato.ac.nz/ml/weka/) and can be found at:

http://storm.cis.fordham.edu/~gweiss/data-mining/weka-data/supermarket.arff

A quick overview of data shows that there was a total of 85762 different purchased items, and the average number of purchased item per transaction was 18.5.

Unfortunately, there is no more detailed information on the extraction and dataset provenance (except that it is originally from NZ). Further observations can also be found at

http://weka.8497.n7.nabble.com/question-of-using-supermarket-arff-for-academic-research-td2573.html
