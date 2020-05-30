import pandas
from sample import Sample

WRONG_KEYS = {"sample", "label"}


class Data:

    def __init__(self, path):
        df = pandas.read_csv(path)
        self.data = df.to_dict(orient="list")
        self.samples = set()

    def create_samples(self):
        """
        This method creates sample objects with id, list of genes values and label.
        Finally adds each object into a set.
        """
        for s_id in range(len(self.data["sample"])):
            genes = []
            for key in self.data.keys():
                # we don't want to append the label value and the sample_id.
                if key not in WRONG_KEYS:
                    genes.append(self.data[key][s_id])
            sample = Sample(s_id, genes, self.data["label"][s_id])
            self.samples.add(sample)
