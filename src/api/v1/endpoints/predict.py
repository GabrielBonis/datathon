from fastapi import APIRouter, Depends
from src.models.predict_input import PredictInput
from src.services.predictor import predict_pipeline
from src.api.v1.endpoints.auth import get_current_user

router = APIRouter()

@router.post("/")
# def predict(data: PredictInput, user: str = Depends(get_current_user)):
def predict(data: PredictInput):
    prediction = predict_pipeline(data)
    return {"prediction": prediction}
