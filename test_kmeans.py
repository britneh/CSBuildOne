from sklearn.cluster import KMeans 

kmeans = KMeans(n_clusters=3)
with open('CSOne.csv','r') as file:
        X = []
        for i, line in enumerate(file):
            if i != 0:
                words = line.split(',')
                row = [words[1]]
                row.append(words[2])
                X.append(row)

kmeans.fit(X)
labels = kmeans.labels_

print(labels)
if __name__ == '__main__':

  # Display first 10 rows:
    print('\n'*2, "*** First 10 rows of X ***")
    print(X[:10])
    print()
            
 
    # Fit the model: assigns each point in X to a cluster
    # kmeans.fit(X)
    # print("*** Centroids ***")
    # print(kmeans.final_cents())
    # print()

    print("*** Clusters ***", kmeans.labels_)
    print()
    
    sample = [[4,20]]
    print(f"*** Prediction for {sample} *** \n", kmeans.predict(sample),'\n')

