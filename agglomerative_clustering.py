import math
from cluster import Cluster


class AgglomerativeClustering:
    # class variable because it stays the same for each run.Therefor no need to build the matrix again.
    distance_matrix = []

    def __init__(self, link, samples):
        self.link = link
        self.samples = samples
        self.clusters = []

    def run(self, max_clusters):
        """
        This method runs the agglomerative clustering algorithm and stops when 'max_clusters' is reached.
        Then prints the data.
        :param max_clusters: number of clusters wanted
        """
        samples_dict = dict()  # dict for s_id and Sample in order to sort the clusters quickly
        for sample in self.samples:
            samples_dict[sample.s_id] = sample
        for index in range(len(self.samples)):
            cluster = Cluster(index, {samples_dict[index]})
            self.clusters.append(cluster)
        # clusters list is sorted in O(n)
        num_of_clusters = len(self.clusters)
        # creates the distance matrix (symmetric matrix) - only one time!
        # because the samples aren't gonna change.
        if not self.distance_matrix:
            for c1_index in range(num_of_clusters):
                distances = []
                for c2_index in range(num_of_clusters):
                    if c2_index > c1_index:
                        # computes the distance between samples.
                        # each 'for loop' runs only 1 time because only one sample exists.
                        for sample1 in self.clusters[c1_index].samples:
                            for sample2 in self.clusters[c2_index].samples:
                                distances.append(sample1.compute_euclidean_distance(sample2))
                    elif c2_index < c1_index:  # creates the symmetric side of the matrix
                        distances.append(self.distance_matrix[c2_index][c1_index])
                    elif c1_index == c2_index:  # diagonal
                        distances.append(-1)
                self.distance_matrix.append(distances)

        # looping through all the clusters and merging the closest
        while num_of_clusters > max_clusters:
            minimal = math.inf
            cluster1_index = 0
            cluster2_index = 0
            for c1_index in range(num_of_clusters):
                cluster1 = self.clusters[c1_index]
                for c2_index in range(c1_index + 1, num_of_clusters):
                    cluster2 = self.clusters[c2_index]
                    dist = self.link.compute(cluster1, cluster2, self.distance_matrix)
                    if dist < minimal:
                        cluster1_index, cluster2_index = c1_index, c2_index
                        minimal = dist
            # merge closest clusters
            self.clusters[cluster1_index].merge(self.clusters[cluster2_index], self.clusters, cluster2_index)
            num_of_clusters -= 1

        # prints data
        for cluster in self.clusters:
            cluster.compute_purity()
            print(cluster)
