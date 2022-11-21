import matplotlib.pyplot as plt
import matplotlib
from sklearn.cluster import KMeans
from app.dataset import read_csv

dataset = read_csv()

featureSelection = ['Variance', 'Skewness', 'Curtosis', 'Entropy']
matplotlib.use('Agg')
def feaSel(a):
    if (a == 0):
        a = featureSelection[0]
    elif (a == 1):
        a = featureSelection[1]
    elif (a == 2):
        a = featureSelection[2]
    elif (a == 3):
        a = featureSelection[3]
    return a

def elbowVis(f1,f2):
    wcss = []
    X = dataset.iloc[:, [f1, f2].values
    for i in range(1, 10):
        kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)

    plt.plot(range(1, 10), wcss)
    plt.title('The Elbow Method')
    plt.xlabel('no of clusters')
    plt.ylabel('wcss')
    plt.savefig('./static/assets/elbow.jpg')
    plt.clf()

