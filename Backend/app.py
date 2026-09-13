from fastapi import FastAPI

import pickle
import pandas as pd
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from model.predict import predict_output, model, MODEL_VERSION

app = FastAPI()


@app.post("/predict")
def predict_premium(data: UserInput):

    user_input={
        "bmi": data.bmi,
        "age_group": data.age_group,
        "lifestyle_risk": data.lifestyle_risk,
        "city_tier": data.city_tier,
        "income_lpa": data.income_lpa,
        "occupation": data.occupation
    }
    try:
        prediction = predict_output(user_input)
        if hasattr(prediction, "item"):
            prediction = prediction.item()

        return JSONResponse(status_code=200, content=prediction)
    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))

@app.get('/')
def home():
    return {"message":"Insurance Premium Prediction API"}

@app.get('/health')
def health_check():
    return {'status':'ok', 'version':MODEL_VERSION}