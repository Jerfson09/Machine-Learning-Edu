import joblib

def predict(data): 
    ridge = joblib.load("Ridge_Regression_model.pkl")

    return ridge.predict(data)