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
                if rand != self.centroid_i[i-1]:
                    #assign each example to closest centroid
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
    
    def find_nearest(self, df, centroids):

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
            
