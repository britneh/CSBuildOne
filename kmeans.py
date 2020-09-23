import numpy as np
import scipy.spatial.distance as scidist

class Kmeans():
    def __init__(self, clusters):
        self.centers = clusters
        self.centroid_i = []
        self.centroids = []
        self.X = None
        self.labels_ = None

    def set_centroids(self):
        i = 0
        while i < self.centers:
            #randomly choose k examples as initial centroids
            random = np.random.randint(len(self.X))
            if i != 0:
                if random != self.centroid_i[i-1]:
                    #assign each example to closest centroid; the more similiar 
                    #the closer to the starting point 
                    self.centroid_i.append(random)
                    i += 1
            else:
                self.centroid_i.append(random)
                i += 1
        for i in self.centroid_i:
            centroid = []
            for j in range(len(self.X[0])):
                centroid.append(self.X[i][j])
            self.centroids.append(centroid)
    
    def get_centroids(self, X, nearest_cent):
        sums = []
        counts = []
        averages = []
        for i in range(len(X[0])):
            sum = [0] * self.centers
            count = [0] * self.centers
            
            for j in range(len(self.X)):
                sum[nearest_cent[j]] += float(self.X[j][i])
                count[nearest_cent[j]] += 1
            sums.append(sum)
            counts.append(count)
        for i in range(len(counts)):
            average = []
            for j in range(len(counts[0])):
                average.append((sums[i][j])/(counts[i][j]))
            averages.append(average)

        averages = list(map(list, zip(*averages)))
        return averages 

    def find_nearest(self, df, cntrds):
        last_cent = [np.random.choice([0,1,2])]*len(X)
        i = 0
        cntrds = self.centroids.copy()
        while True:
            if i>0:
                cntrds = self.get_centroids(X, last_cent)
            distances = scidist.cdist(X, cntrds)
            nearest_cent = np.argmin(distances, axis =1)

            if (list(nearest_cent) == list(last_cent)):
                centroids = cntrds
                return nearest_cent
            else:
                i += 1
                last_cent = nearest_cent 

    def fit(self, X):
        self.X = X
        self.set_centroids()
        self.labels = self.find_nearest(self.X, self.centroids)

    def predict(self, X):
        distance = scidist.cdist(X, self.centroids)
        mins = []
        mins_i = []
        for i in distance:
            minimum = np.min(i)
            mins.append(minimum)
            mins_i.append(np.where(i == minimum)[0][0])
        return mins_i

    
    def final_cents(self):
        for i in self.centroids:
            print(i)

if __name__ == '__main__':
    # Read in data from csv to X
    with open('CSOne.csv','r') as file:
        X = []
        for i, line in enumerate(file):
            if i != 0:
                words = line.split(',')
                row = [words[1]]
                row.append(words[2])
                X.append(row)

    # Display first 10 rows:
    print('\n'*2, "*** First 10 rows of X ***")
    print(X[:10])
    print()
            
  # Create new KMeans object
    kmeans = Kmeans(3)

    # Fit the model: assigns each point in X to a cluster
    kmeans.fit(X)
    print("*** Centroids ***")
    print(kmeans.final_cents())
    print()

    print("*** Clusters ***", kmeans.labels)
    print()
    
    sample = [[6,9],[6,11]]
    print(f"*** Prediction for {sample} *** \n", kmeans.predict([[6,9],[6,11]]),'\n')