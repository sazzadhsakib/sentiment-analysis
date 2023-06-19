from fastapi import APIRouter, Body
from src.data.models.detect_sentiment_request_model import DetectSentimentRequestModel
from src.data.models.detect_sentiment_response_model import DetectSentimentResponseModel
from src.usecases.detect_sentiment_uc import DetectSentimentUC

router = APIRouter()

@router.post('/analyze', response_model=DetectSentimentResponseModel)
async def detectSentiment(
    request: DetectSentimentRequestModel,
):
    detectSentimentRequestModel = DetectSentimentRequestModel(text=request.text)
    usecase = DetectSentimentUC()
    return await usecase(detectSentimentRequestModel)
    
