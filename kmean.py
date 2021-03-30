import csv
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN


def csv_points():
    with open(file="Lidar.csv", newline='') as csvfile:
        read = csv.reader(csvfile, delimiter=',')
        for x, y, z in read:
            yield float(x), float(y), float(z)


if __name__ == '__main__':
    read_points = list(csv_points())
    X, Y, Z = zip(*read_points)
    p = np.array(read_points)

    cluster = DBSCAN(eps=15, min_samples=10).fit(p)
    labels = cluster.labels_

    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
    n_noise_ = list(labels).count(-1)

    print('Estimated number of clusters: %d' % n_clusters_)
    print('Estimated number of noise points: %d' % n_noise_)

    n_clusters = 3
    k_means = KMeans(n_clusters=n_clusters)
    k_means = k_means.fit(p)
    labels = k_means.predict(p)

    red = labels == 0
    green = labels == 1
    blue = labels == 2

    fig_2 = plt.figure()
    ax_2 = fig_2.add_subplot(projection='3d')
    ax_2.scatter(p[red, 0], p[red, 1], p[red, 2], marker='o')
    ax_2.scatter(p[green, 0], p[green, 1], p[green, 2], marker='^')
    ax_2.scatter(p[blue, 0], p[blue, 1], p[blue, 2], marker='x')
    plt.show()