import numpy as np
import matplotlib.pyplot as plt
from sklearn import cluster
from scipy.spatial import distance

points = []
labels = []

file = open('cluster_data.tsv')
for line in file:
    data = line.strip().split('\t')

    point = (float(data[0]), float(data[1]))
    cluster_id = int(data[2])

    points.append(point)
    labels.append(cluster_id)

points = np.asarray(points)

# plt.scatter(points[:, 0], points[:, 1], color=[plt.cm.spectral(l/20.0) for l in labels])
# plt.show()

n_class = 20

k_means = cluster.KMeans(init='random', n_clusters=n_class, n_init=5)
k_means.fit(points)
sse = 0
for point, label in zip(points, k_means.labels_):
    sse += distance.euclidean(point, k_means.cluster_centers_[label]) ** 2
print "KMeans   SSE: %.8f" % sse

plt.scatter(points[:, 0], points[:, 1], color=[plt.cm.spectral(l/20.0) for l in k_means.labels_])
plt.show()

k_means_pp = cluster.KMeans(init='k-means++', n_clusters=n_class, n_init=5)
k_means_pp.fit(points)
plt.scatter(points[:, 0], points[:, 1], color=[plt.cm.spectral(l/20.0) for l in k_means_pp.labels_])
plt.show()

sse = 0
for point, label in zip(points, k_means_pp.labels_):
    sse += distance.euclidean(point, k_means_pp.cluster_centers_[label]) ** 2
print "KMeans++ SSE: %.8f" % sse