from math import sqrt


class Sample:

    def __init__(self, s_id, genes, label):
        self.s_id = s_id
        self.genes = genes
        self.label = label

    def compute_euclidean_distance(self, other):
        """
        This method computes the euclidean distance between 2 samples.
        :param other: Object of class Sample.
        :return: Euclidean distance
        """
        sum_of_distances = 0
        for i in range(len(self.genes)):
            sum_of_distances += (self.genes[i] - other.genes[i]) ** 2
        return sqrt(sum_of_distances)
