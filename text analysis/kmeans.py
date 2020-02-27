#Taken from https://datasciencelab.wordpress.com/2013/12/12/clustering-with-k-means-in-python/
# Just added plotting for 3-k cases

import numpy as np
import random
import matplotlib.pyplot as plt

def init_board(N):
    X = np.array([(random.uniform(-1, 1), random.uniform(-1, 1)) for i in range(N)])
    return X

def cluster_points(X, mu):
    clusters  = {}
    for x in X:
        bestmukey = min([(i[0], np.linalg.norm(x-mu[i[0]])) \
                    for i in enumerate(mu)], key=lambda t:t[1])[0]
        try:
            clusters[bestmukey].append(x)
        except KeyError:
            clusters[bestmukey] = [x]
    return clusters

def reevaluate_centers(mu, clusters):
    newmu = []
    keys = sorted(clusters.keys())
    for k in keys:
        newmu.append(np.mean(clusters[k], axis = 0))
    return newmu

def has_converged(mu, oldmu):
    return (set([tuple(a) for a in mu]) == set([tuple(a) for a in oldmu]))

def find_centers(X, K):
    # Initialize to K random centers
    oldmu = random.sample(X, K)
    mu = random.sample(X, K)
    while not has_converged(mu, oldmu):
        oldmu = mu
        # Assign all points in X to clusters
        clusters = cluster_points(X, mu)
        # Reevaluate centers
        mu = reevaluate_centers(oldmu, clusters)
    return(mu, clusters)

def change_coords(array):
    return list(map(list, zip(*array)))

def parse_output(data):
    clusters = data[1]
    points1 = change_coords(clusters[0])
    plt.plot(points1[0], points1[1], 'ro')
    points2 = change_coords(clusters[1])
    plt.plot(points2[0], points2[1], 'g^')
    points3 = change_coords(clusters[2])
    plt.plot(points3[0], points3[1], 'ys')
    centroids = change_coords(data[0])
    plt.plot(centroids[0], centroids[1], 'kx')
    plt.axis([-1.0, 1, -1.0, 1])
    plt.show()

data1 = init_board(15)
print(data1)
data = np.array( [[0.53,0.666],[0.98,0.34],
[0.7745,0.453],[0.231,0.222],
[0.523,0.111],[0.325,0.666],
[-0.935,-0.253],[-0.543,-0.324],
[-0.7734,-0.554],[-0.834,-0.434],
[0.123,-0.232],[0.321,-0.121],
[0.386,-0.264],[0.409,-0.4323],
[0.302,-0.178]])
print(data)
print(type(data))
out = find_centers(list(data), 3)
parse_output(out)