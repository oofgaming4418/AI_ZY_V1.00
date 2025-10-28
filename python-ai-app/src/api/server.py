from fastapi import FastAPI
from pydantic import BaseModel
from src.models.model import Model
from src.data.dataset import Dataset

app = FastAPI()
model = Model()
dataset = Dataset()

class PredictionRequest(BaseModel):
    input_data: list

@app.on_event("startup")
def load_model():
    model.load("path/to/model")  # Load the trained model

@app.post("/predict")
def predict(request: PredictionRequest):
    processed_data = dataset.preprocess(request.input_data)
    prediction = model.predict(processed_data)
    return {"prediction": prediction}