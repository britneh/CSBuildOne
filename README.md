
# How to use K-means Algorithm 

K-means Clustering is dividing a dataset into groups, consisting of similiar data points 
    - Group of diners 
        People at different tables not related to each other
    - Items arranged in a grocery store
        Similiar items are grouped together; produce

Netflix, Amazon - use to make recommendations, based on previous purchases are previously watched 

The csv for this project was created in another notebook and then imported inside for use with the algorithm.  You can find associated code in create.ipynb.

K- means clustering can be broken down into 4 steps: 

* Step 1: Pick k random points as cluster centers.  Here, 'k' represents the number of clusters; for this example I have chosen ‘3’. Depending on your data, the amount of k could be predetermined. However, in other cases you may have to use your best judgement. Thankfully, this algorithm makes it easy to test out different k’s. The ‘set_centroids’ method uses the  NumPy random library to choose points from the data set. These points are just temporary markers for the center of the clusters. They will change as we move through the algorithm to find the most optimal centers, also referred to as centroids.

* Step 2: Assign each data point to the nearest cluster. The next method created was ‘find_nearest’. Once the initial centroids have been identified, we can group other data points to them by calculating the shortest distance (also known as euclidean distance) from the data points to the centroids. Meaning, the closer a data point is to a centroid, the more likely it relates to other data points with similar distances. These data points are combined to create the cluster.

* Step 3: Find a new cluster center by taking the average of assigned points. Because we started with temporary centroids, we must attempt to get as close as we can to the ‘real’ center for the most optimal clustering. The method that provides this functionality is ‘get_centroids’. The cluster center is found by taking the average of the assigned points. 

* Step 4: Repeat steps 2 and 3 until the cluster assignments are not changed. Once the new cluster center is determined we want to repeat the process of calculating new centroids and getting clusters for those new centroids until there are no changes in cluster assignments, meaning we have reached convergence which is the most optimal state. 

To make fit and make predictions: 
The ‘fit’ method uses both ‘set_centroids’ and ‘find_nearest’ to label the dataset so that once we implement the ‘predict’ method with our sample data points, it can recommend the best cluster assignment. 

## test_kmeans.py uses the Sci-kit learn Kmeans
Use test_kmeans.py to compare the algorithm predictions to that of Sci-kit learn

K means is best used when the number of cluster centers is specified to well defined list of types so that you can best determine k.

