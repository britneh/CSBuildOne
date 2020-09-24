1. Pick k random points as cluster centers
2. assign each xi to nearest cluster by calculating distance to each centroid (euclidean distance)
3. Find new cluster center by taking the average of assigned points
4. Repeat step 2-3 until none of the cluster assignments change 

Clustering is dividing a dataset into groups, consisting of similiar data points 
    - Group of diners 
        People at different tables not related to each other
    - Items arranged in a grocery store
        Similiar items are grouped together; produce

Netflix, Amazon - use to make recommendations, based on previous purchases are previously watched 

Kmeans is a type of exclusive clustering.  There also exists overlapping and heirarchical clustering. 


Step 1: 
Select the number of clusters to be identified

Step 2: Randomly select 3 distinct data points

Step 3: Measure distance between the first point and the 3 clusters 


Created a csv in another notebook and imported inside for use with the algorithm.  


K means is best used when the number of cluster centers is specified to well defined list of types. 