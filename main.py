from flask import Flask, render_template, request, flash, session
# from flask_ngrok import run_with_ngrok

import sklearn
from app.elbow import elbowVis, feaSel
from app.dataset import read_csv
# from app.plot import plotVis
dataset = read_csv

from flask_toastr import Toastr
import os


app = Flask(__name__)

# run_with_ngrok(app)
app.secret_key="HoshimachiSuiseiUwU"
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

    if ((not f1=='') and (not f2=='')):
        elbowVis(int(f1),int(f2))
        a = feaSel(int(f1))
        b = feaSel(int(f2))
        return render_template("index.html", outputfeature=f"F1: {a} \t F2: {b}")
    else:
        flash("Hoshimachi Suisei aren't features")
        return render_template("index.html", outputfeature=f"No Feature Choosen")


@app.route('/plot',methods=["GET",'POST'])
def plot():
    f1 = session.get('f1', None)
    f2 = session.get('f2', None)
    k = request.form.get("kvalue")
    if ((not f1=='') and (not f2=='')):
        plotVis(f1,f2,k)
        return render_template("index.html")
    else:
        flash("No New Features Selected")
        return render_template("index.html")

if __name__ == '__main__':
	app.run(debug=True)