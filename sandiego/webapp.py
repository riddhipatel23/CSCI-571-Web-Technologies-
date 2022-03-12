import numpy as np
from flask import Flask, render_template,request, redirect, url_for, session
import pickle
import pandas as pd
from collections import defaultdict
import model

app = Flask(__name__)
#model = pickle.load(open('regr.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('./home.html')


@app.route('/predict', methods =['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    prediction = model.load(int_features[0], int_features[1])
    return render_template('home.html', result = prediction)

if __name__ == "__main__":
    app.run(debug=True)
