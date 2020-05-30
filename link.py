import abc

from cluster import Cluster


class Link:
    @abc.abstractmethod
    def compute(self, cluster, other, distances=None):
        pass


class SingleLink(Link):

    def compute(self, cluster, other, distances=None):
        """
        This method computes minimum distances between two different clusters.
        :param cluster: First object of Cluster
        :param other: Second object of Cluster
        :param distances: matrix of distances
        :return: Distance
        """
        minimum = False
        for sample1 in cluster.samples:
            for sample2 in other.samples:
                dist = distances[sample1.s_id][sample2.s_id]
                if minimum is False or dist < minimum:
                    minimum = dist
        return minimum


class CompleteLink(Link):

    def compute(self, cluster, other, distances=None):
        """
        This method computes maximum distances between two different clusters.
        :param cluster: First object of Cluster
        :param other: Second object of Cluster
        :param distances: matrix of distances
        :return: Distance
        """
        maximum = 0
        for sample1 in cluster.samples:
            for sample2 in other.samples:
                dist = distances[sample1.s_id][sample2.s_id]
                if dist > maximum:
                    maximum = dist
        return maximum
