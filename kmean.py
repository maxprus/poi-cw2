from sklearn.cluster import KMeans
from scipy.stats import norm

import matplotlib.pyplot as plt
import numpy as np
import csv

#Wczytywanie chmury
def cloud_reader():
    with open('Lidar.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for x, y, z in reader:
            yield (float(x), float(y), float(z))

for p in cloud_reader():


"""
mns = [(5, 3), (15, 4), (10, 8)]
scales = [(2, 1), (1, 1), (1, 2)]


params = zip(mns, scales)

clusters = []

for parset in params:
    dist_x = norm(loc=parset[0][0], scale=parset[1][0])
    dist_y = norm(loc=parset[0][1], scale=parset[1][1])
    cluster_x = g(x)
    cluster_y = g(y)
    cluster_z = g(z)
    cluster = zip(cluster_x, cluster_y, cluster_z)
    clusters.extend(cluster)

x, y = zip(*clusters)
plt.figure()
plt.scatter(x, y)
plt.title('Points scattering in 2D')
plt.tight_layout()
plt.xlabel('x')


clusterer = KMeans(n_clusters=3)

X = np.array(clusters)
y_pred = clusterer.fit_predict(X)

red = y_pred == 0
blue = y_pred == 1
cyan = y_pred == 2

plt.figure()
plt.scatter(X[red, 0], X[red, 1], c="red")
plt.scatter(X[blue, 0], X[blue, 1], c="blue")
plt.scatter(X[cyan, 0], X[cyan, 1], c="cyan")
plt.show()
"""

