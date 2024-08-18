import joblib

def predict(data): 
    ridge = joblib.load("Linear_model.pkl")

    return ridge.predict(data)