# 🧠 Customer Churn Predictor (Docker + FastAPI)

This is my first full MLOps project where I took a machine learning model, wrapped it in a FastAPI app, and deployed it in a Docker container. If you’re new to this stuff — it means I trained a model to guess if a customer is about to leave, then built a little API around it that anyone can run and test.

---

## 🔧 What’s Inside

- 🧪 Trained a Scikit-learn model to predict churn  
- 🛠️ FastAPI app that loads the model and handles predictions  
- 🐳 Dockerfile so the whole thing can run in a container  
- 📦 requirements.txt for dependencies  
- 📊 Notebooks for EDA, training, and MLflow logging  

---

## Build the container
bash-
docker build -t churn-api .
## Run the app
bash-
docker run -p 8000:8000 churn-api
## Now open your browser to:
bash-
http://localhost:8000/docs
You'll see the Swagger UI where you can test the /predict endpoint.

## 🔍 Sample Input for /predict
Here’s what to send in as JSON:

json-
{
  "Gender": 1,
  "Age": 35,
  "Tenure": 5,
  "Balance": 75000.0,
  "NumOfProducts": 2,
  "IsActiveMember": 1,
  "EstimatedSalary": 50000.0,
  "Geography": 1,
  "HasCrCard": 1,
  "CreditScore": 620
}
## It’ll respond with something like:

json-
{
  "churn_prediction": 1
}
## 📦 Files & Folders
Path	Purpose
api/	FastAPI app code
model/	Serialized .pkl model
notebooks/	EDA + training + tracking
Dockerfile	Build config for the container
requirements.txt	All the Python dependencies

🚀 Why I Built This
Curious about MLOps and wanted to actually build something I could test, run in Docker, and eventually deploy. This repo is part of my portfolio I am trying to build while in school.