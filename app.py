# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 15:54:50 2021

@author: joshi
"""
from flask import Flask, render_template, request
import os
import jsonify
import requests
import pickle
import numpy as np
import joblib
from sklearn import *
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('logistic_reg.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        age = int(request.form['age'])
        trestbps = float(request.form['trestbps'])
        chol = int(request.form['chol'])
        thalach = int(request.form['thalach'])  
        oldpeak = float(request.form['oldpeak'])
        Gender = int(request.form['gender'])
        sex_1 = 0
        sex_0 = 0
        if Gender == 0:
            sex_0 = 1
        else:
            sex_1 = 1
        ChestPain = int(request.form['chest_pain'])
        cp_0 = 0
        cp_1 = 0
        cp_2 = 0
        cp_3 = 0
        if(ChestPain == 0):
            cp_0 = 1
        elif(ChestPain == 1):
            cp_1 = 1
        elif(ChestPain == 2):
            cp_2 = 1
        else:
            cp_3 = 1
        FastingBloodSugar = int(request.form['fbs'])
        fbs_0 = 0
        fbs_1 = 0
        if(FastingBloodSugar == 0):
            fbs_0 = 1
        else:
            fbs_1 = 1
        RestingEKGResults = int(request.form['restecg'])
        restecg_0 = 0
        restecg_1 = 0
        restecg_2 = 0
        if(RestingEKGResults == 0):
            restecg_0 = 1
        elif(RestingEKGResults == 1):
            restecg_1 = 1
        else:
            restecg_2 = 1
        Exang = int(request.form['exang'])
        exang_0 = 0
        exang_1 = 0
        if(Exang == 0):
            exang_0 = 1
        else:
            exang_1 = 1
        Slope = int(request.form['slope'])
        slope_0 = 0
        slope_1 = 0
        slope_2 = 0
        if(Slope == 0):
            slope_0 = 1
        elif(Slope == 1):
            slope_1 = 1
        else:
            slope_2 = 1
        CA = int(request.form['ca'])
        ca_0 = 0
        ca_1 = 0
        ca_2 = 0
        ca_3 = 0
        ca_4 = 0
        if(CA == 0):
            ca_0 = 1
        elif(CA == 1):
            ca_1 = 1
        elif(CA == 2):
            ca_2 = 1
        elif(CA == 3):
            ca_3 = 1
        else: 
            ca_4 = 1
        Thal = int(request.form['thal'])
        thal_0 = 0
        thal_1 = 0
        thal_2 = 0
        thal_3 = 0 
        if(Thal == 0):
            thal_0 = 1
        elif(Thal == 1):
            thal_1 = 1
        elif(Thal == 2):
            thal_2 = 1
        else:
            thal_3 = 1
        prediction=model.predict([[age, trestbps, chol, thalach, oldpeak, sex_0, sex_1, cp_0, cp_1, cp_2, cp_3, fbs_0, fbs_1, restecg_0, restecg_1, restecg_2, exang_0, exang_1, slope_0, slope_1, slope_2, ca_0, ca_1, ca_2, ca_3, ca_4, thal_0, thal_1, thal_2, thal_3]])
        print(prediction)
        if prediction[0] == 0:
            return render_template('index.html',prediction_text="You have very low chances of heart disease!")
        else:
            return render_template('index.html',prediction_text="You have higher risk of having a heart disease")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
