class Cluster:

    def __init__(self, c_id, samples):
        self.c_id = c_id
        self.samples = samples
        self.dominant_label = ""
        self.purity = 0

    def merge(self, other, clusters, index):
        """
        This method merges two cluster objects and removes the unnecessary(other).
        :param other: object of cluster.
        :param clusters: this list of clusters.
        :param index: index of other cluster in the list
        """
        self.c_id = min(self.c_id, other.c_id)
        self.samples.update(other.samples)
        clusters.pop(index)

    def compute_purity(self):
        """
        This function computes the purity of the cluster and find the dominant label.
        """
        labels_dict = {
            "BRCA": 0,
            "COAD": 0,
            "KIRC": 0,
            "LUAD": 0,
            "PRAD": 0
        }
        total_sum = 0
        max_value = 0
        dominant_label = ""
        for sample in self.samples:
            label = sample.label
            labels_dict[label] += 1
            if labels_dict[label] > max_value:
                max_value = labels_dict[label]
                dominant_label = label
            total_sum += 1
        self.dominant_label = dominant_label
        self.purity = labels_dict[dominant_label] / total_sum

    def __str__(self):
        """
        This method edits the print option of the class.
        :return: print format
        """
        return f"Cluster {self.c_id}: {sorted([sample.s_id for sample in self.samples])}, " \
               f"dominant label: {self.dominant_label}, purity: {self.purity}"
