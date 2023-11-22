###################################################
# app.py
# User interface to make predictions using Flask
###################################################

from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
from mlProject.pipeline.prediction import PredictionPipeline


app = Flask(__name__) # initializing a flask application

@app.route('/', methods=['GET']) # defining a route to display home page
def homepage():
    return render_template("index.html") # opens up index.html


@app.route('/train', methods=['GET']) # defining a route to display training page
def training():
    os.system("python main.py")
    return "Training Has Finished Successfully!"

@app.route('/predict', methods=['POST', 'GET']) # defining a route to display as prediction page
def index():
    if request.method == 'POST':
        try:
            # gets inputs from user
            fixed_acidity = float(request.form['fixed_acidity'])
            volatile_acidity = float(request.form['volatile_acidity'])
            citric_acid = float(request.form['citric_acid'])
            residual_sugar =float(request.form['residual_sugar'])
            chlorides =float(request.form['chlorides'])
            free_sulfur_dioxide =float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide =float(request.form['total_sulfur_dioxide'])
            density =float(request.form['density'])
            pH =float(request.form['pH'])
            sulphates =float(request.form['sulphates'])
            alcohol =float(request.form['alcohol'])
         
            # creates numpy array from the data gathered
            data = [fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,
                    total_sulfur_dioxide,density,pH,sulphates,alcohol]
            data = np.array(data).reshape(1,11)

            # make prediction
            pred_pipline = PredictionPipeline()
            prediction = pred_pipline.predict(data)

            return render_template('results.html', prediction=str(prediction))
        
        except Exception as e:
            raise e
    else:
        return render_template("index.html")



if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=8080, debug=True)
    app.run(host="0.0.0.0", port=8080)
    
