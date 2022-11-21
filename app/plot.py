import matplotlib.pyplot as plt
import matplotlib
from sklearn.cluster import KMeans
from app.dataset import read_csv

dataset = read_csv()
clr = ['red','yellow','blue','green','pink','cyan','magenta','orange','black','purple']
def plotVis(f1,f2,k):
    X= dataset.iloc[:, [int(f1),int(f2)]].values
    kmeansmodel = KMeans(n_clusters= int(k), init='k-means++', random_state=0)
    y_kmeans= kmeansmodel.fit_predict(X)
    colname = list(dataset.columns)
    for i in range(int(k)):
        plt.scatter(X[y_kmeans == i, 0], X[y_kmeans == i, 1], s = 30, c = clr[i], label = f'Cluster {i+1}')
    plt.title('Clusters IRIS')
    plt.xlabel(colname[int(f1)])
    plt.ylabel(colname[int(f2)])
    plt.legend()
    plt.savefig('./static/assets/vis.jpg')
    plt.clf()