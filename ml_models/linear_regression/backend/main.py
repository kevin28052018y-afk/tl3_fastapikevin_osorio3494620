import joblib
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("model/linear_regression_model.joblib")

class AreaInput(BaseModel):
    area: float

@app.get("/predict")
def get_predict():
    return [{"area": a, "precio": float(model.predict([[a]])[0])} for a in range(70, 151, 10)]

@app.post("/predict")
def post_predict(data: AreaInput):
    return {"area": data.area, "precio": float(model.predict([[data.area]])[0])}