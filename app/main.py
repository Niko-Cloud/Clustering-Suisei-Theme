from flask import Flask, render_template, request, flash, session
# from flask_ngrok import run_with_ngrok
import pandas as pd
import sklearn
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import matplotlib
from flask_toastr import Toastr
import os
matplotlib.use('Agg')

app = Flask(__name__)

# run_with_ngrok(app)
app.secret_key="HoshimachiSuiseiUwU"

dataset = pd.read_csv('./BankNote_Authentication.csv')
clr = ['red','yellow','blue','green','pink','cyan','magenta','orange','black','purple']

toastr = Toastr(app)

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():

    if os.path.exists("./static/assets/vis.jpg"):
        os.remove("./static/assets/vis.jpg")

    if os.path.exists("./static/assets/elbow.jpg"):
        os.remove("./static/assets/elbow.jpg")

    return render_template("index.html")


@app.route('/feature',methods=["GET",'POST'])
def feature():
    session['f1'] = request.form.get("feature1")
    session['f2'] = request.form.get("feature2")

    f1 = request.form.get("feature1")
    f2 = request.form.get("feature2")

    featureSelection = ['Variance', 'Skewness', 'Curtosis', 'Entropy']

    def feaSel(a):
        if(a==0):
            a=featureSelection[0]
        elif(a==1):
            a=featureSelection[1]
        elif(a==2):
            a=featureSelection[2]
        elif(a==3):
            a=featureSelection[3]
        return a

    if ((not f1=='') and (not f2=='')):
        wcss=[]
        X= dataset.iloc[:, [int(f1),int(f2)]].values
        for i in range(1,10):
            kmeans = KMeans(n_clusters= i, init='k-means++', random_state=42)
            kmeans.fit(X)
            wcss.append(kmeans.inertia_)

        plt.plot(range(1,10), wcss)
        plt.title('The Elbow Method')
        plt.xlabel('no of clusters')
        plt.ylabel('wcss')
        plt.savefig('./static/assets/elbow.jpg')
        plt.clf()
        a=feaSel(int(f1))
        b=feaSel(int(f2))
        return render_template("index.html", outputfeature=f"F1: {a} \t F2: {b}")
    else:
        flash("Hoshimachi Suisei aren't features")
        return render_template("index.html", outputfeature=f"No Feature Choosen")


@app.route('/plot',methods=["GET",'POST'])
def plot():
    f1 = session.get('f1', None)
    f2 = session.get('f2', None)
    k = requepythost.form.get("kvalue")
    if ((not f1=='') and (not f2=='')):
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
        return render_template("index.html")
    else:
        return render_template("index.html")

