from enum import Enum
from pydantic import BaseModel, Field
from fastapi import FastAPI, HTTPException, Path, Query
import pickle

app = FastAPI()

filename = "logit_model.pkl"
model = pickle.load(open(filename, "rb"))


class ModelInput(BaseModel):
    age: float
    income: float
    loan: float

class ModelOutput(BaseModel):
    point_prediction: float
    prediction_lower_bound: float
    prediction_upper_bound: float


@app.get("/")
async def root():
    """Return default message"""
    return {"message": "Hello World."}


@app.get("/info")
async def model_info():
    """Return model information, version, how to call"""
    return {"name": "Logit", "version": "1.0"}


@app.post("/predict")
async def predict(item: ModelInput):
    predictions = model.get_prediction(item.dict()).summary_frame()
    output = ModelOutput(
        point_prediction=predictions["predicted"],
        prediction_lower_bound=predictions["ci_lower"],
        prediction_upper_bound=predictions["ci_upper"],
    )

    return output
