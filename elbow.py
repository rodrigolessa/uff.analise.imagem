
import pickle, argparse, re, time
import os
import numpy as np
from utils import Log
import pandas as pd

from sklearn import metrics
from sklearn.metrics import pairwise_distances
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
from sklearn.cluster import KMeans, MiniBatchKMeans

ap = argparse.ArgumentParser()
ap.add_argument("-m", "--moments_folder" , required = True, help = "Moments folder")
args = vars(ap.parse_args())

moments_folder = args['moments_folder']

# degrees = [11, 23, 43, 50]
degrees = [43]

for degree in degrees:
    sls = []
    chs = []

    inertia_list = []

    print("- order: {}".format(degree))

    # open moments dataset for current degree
    dataset = pd.read_csv(open("{}/moments{}.csv".format(moments_folder, degree)), header=None, sep=';', index_col=None)
    X = dataset.iloc[:, 1:]

    # kc = list(range(10, 100, 10))
    # kc = list(range(1000, 100001, 1000))
    kc = list(range(10, 101, 10))

    for k_clusters in kc:
        print(k_clusters)
        # kmeans = MiniBatchKMeans(n_clusters=k_clusters, random_state=42, verbose=1)
        cluster_path = "tests/elbow/{}-{}.cluster".format(degree, k_clusters)
        if os.path.exists(cluster_path):
            kmeans = pickle.load(open(cluster_path, "rb"))
        else:
            kmeans = KMeans(n_clusters=k_clusters, random_state=42, verbose=1)
            kmeans.fit(X)
            pickle.dump(kmeans, open(cluster_path, "wb"))

        # --- não supervisionada
        inertia_list.append(kmeans.inertia_)

        # #--- supervisionada
        # print("labels")
        # labels = kmeans.fit_predict(X)
        # pickle.dump(kmeans, open("tests/{}.cluster".format(k_clusters), "wb"))
        # sls.append(metrics.silhouette_score(X, labels, metric='mahalanobis'))
        # chs.append(metrics.calinski_harabaz_score(X, labels))

    fig, ax=plt.subplots()

    # #--- supervisionada
    # plt.subplot(1,1,1)
    # plt.title('silhouette_score')
    # plt.xlabel('codebook size')
    # plt.plot(kc, sls, 'r')

    # plt.subplot(2,1,2)
    # plt.title('calinski_harabaz_score')
    # plt.xlabel('codebook size')
    # plt.plot(kc, chs, 'b')

    # print(sls)
    # print(chs)

    # --- não supervisionada 
    plt.subplot(1,1,1)
    plt.title('inertia')
    plt.xlabel('codebook size')
    plt.plot(kc, inertia_list, 'r')

    intervals = 50
    loc = plticker.MultipleLocator(base=intervals)
    ax.yaxis.set_major_locator(loc)
    ax.grid(which='major', axis='y', linestyle='-')

    print(inertia_list)

    plt.savefig('tests/elbow/{}-kmeans-scores.png'.format(degree))