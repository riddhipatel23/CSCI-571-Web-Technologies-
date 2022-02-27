import numpy as np
from flask import Flask, render_template,request, redirect, url_for, session
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import re
from collections import defaultdict

#Initialize the flask App
app = Flask(__name__)
biased_model = pickle.load(open('biased.pkl', 'rb'))
unbiased_model = pickle.load(open('unbiased.pkl', 'rb'))

#default page of our web-app
@app.route('/')
def home():
    return render_template('./home.html')

@app.route('/home.html')
def home1():
    return render_template('./home.html')
# @app.route('/model', methods=['POST'])
# def model():

@app.route('/summary.html')
def summary():
    return render_template('./summary.html')

@app.route('/prediction_page.html')
def prediction_page():
    return render_template('./prediction_page.html')

@app.route('/predict', methods =['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    if int_features[0] == 0:
        prediction = biased_model.predict([[int_features[1], int_features[2], int_features[3]]])
    else:
        prediction = unbiased_model.predict([[int_features[1], int_features[2]]])
       
    return render_template('prediction_page.html', income = prediction)

if __name__ == "__main__":
    app.run(debug=True)






     

