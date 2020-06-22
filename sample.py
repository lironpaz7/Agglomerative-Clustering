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
        return sqrt(sum([(x - y) ** 2 for x, y in zip(self.genes, other.genes)]))
