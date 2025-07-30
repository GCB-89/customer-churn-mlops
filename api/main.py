# === 🌐 FastAPI Churn Prediction Service ===
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

""" For some reason I have to put uvicorn api.main:app --reload
in the terminal to run this file, even though I have the FastAPI extension installed in VSCode."""

# 🚀 Start FastAPI app
app = FastAPI(title="Customer Churn Predictor")

# 🔄 Load the trained model (make sure path is correct)
model = joblib.load("./model/churn_model.pkl")





# 📦 Define input data structure
class ChurnInput(BaseModel):
    Gender: int
    Age: int
    Tenure: int
    Balance: float
    NumOfProducts: int
    IsActiveMember: int
    EstimatedSalary: float

# 🏠 Root route
@app.get("/")
def read_root():
    return {"message": "🔥 Churn Prediction API is live!"}

# 🔮 Prediction route
@app.post("/predict")
def predict_churn(data: ChurnInput):
    # Turn incoming data into the format the model expects
    input_array = np.array([[
        data.Gender,
        data.Age,
        data.Tenure,
        data.Balance,
        data.NumOfProducts,
        data.IsActiveMember,
        data.EstimatedSalary
    ]])
    
    # Run prediction
    prediction = model.predict(input_array)[0]
    label = "Will Churn" if prediction == 1 else "Will Stay"
    
    return {
        "prediction": int(prediction),
        "label": label
    }
