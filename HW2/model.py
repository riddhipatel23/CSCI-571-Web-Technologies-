import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib


def train():
    df = pd.read_csv("./static/SBP.csv")

    x = df[["Age", "Weight"]]
    y = df["SBP"]

    regr = LinearRegression()
    regr.fit(x, y)

    joblib.dump(regr, "regr.pkl")


def load(age,weight):
    clf = joblib.load("regr.pkl")
    #age = 18
    #weight = 19
    x = pd.DataFrame([[age, weight]], columns=["Age", "Weight"])
    prediction = clf.predict(x)[0]
    return prediction


if __name__ == "__main__":
    train()
    load(18,19)
