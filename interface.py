import re
from flask import Flask, jsonify, render_template, request,redirect, url_for
import config
from project_app.utils import WeightPrediction

app = Flask(__name__)

@app.route('/predict_weight',methods = ['POST','GET'])

def get_fish_weight():
    if request.method == 'POST':
        print("We are using POST method")
        data = request.form
        Length1 = eval(data["Length1"])
        Length2 = eval(data["Length2"])
        Length3 = eval(data["Length3"])
        Height = eval(data["Height"])
        Width = eval(data["Width"])
        Species = data["Species"]


        wgt_pre = WeightPrediction(Length1, Length2, Length3, Height, Width, Species)
        weight = wgt_pre.get_predicted_weight()
        return jsonify({"Weight": f"Predicted Weight of Fish is : {weight}"})

    else:
        print("We are using GET method")
        # if we want to directly predict ans then pass values below
        Length1 = 23.20
        Length2 = 25.40
        Length3 = 30.00
        Height = 11.52
        Width = 4.02
        Species = 'Parkki'

        wgt_pre = WeightPrediction(Length1, Length2, Length3, Height, Width, Species)
        weight = wgt_pre.get_predicted_weight()
        return jsonify({"Weight": f"Predicted Weight of Fish is : {weight}"})


@app.route('/') 
def main():
    return render_template('index.html')


@app.route('/predict',methods = ['POST','GET'])
def predict():
    if request.method == 'POST':
        
        data = request.form
        Length1 = eval(data["Length1"])
        Length2 = eval(data["Length2"])
        Length3 = eval(data["Length3"])
        Height = eval(data["Height"])
        Width = eval(data["Width"])
        Species = data["Species"]
        
        object = WeightPrediction(Length1, Length2, Length3, Height, Width, Species)
        prediction = object.get_predicted_weight()

        return render_template("result.html", prediction = prediction)


if __name__ == "__main__":
    app.run(host= '0.0.0.0', port = 8080,debug=False)
