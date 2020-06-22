import time
import sys
from data import Data
from link import SingleLink, CompleteLink
from agglomerative_clustering import AgglomerativeClustering


def main(argv):
    start = time.time()
    dt = Data(argv[1])
    dt.create_samples()
    links = argv[2].replace("_", " ").split(", ")
    max_clusters = int(argv[3])
    single_link = SingleLink()
    complete_link = CompleteLink()
    run1 = AgglomerativeClustering(single_link, dt.samples)
    run2 = AgglomerativeClustering(complete_link, dt.samples)
    print(f"{links[0]}:")
    run1.run(max_clusters)

    print()
    print()

    print(f"{links[1]}:")
    run2.run(max_clusters)

    print()

    end = time.time()
    print(f"Total run time: {end - start} seconds")


if __name__ == "__main__":
    main(sys.argv)
