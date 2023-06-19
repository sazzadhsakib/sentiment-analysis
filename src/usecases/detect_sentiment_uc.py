from src.data.models.detect_sentiment_request_model import DetectSentimentRequestModel
from src.data.models.detect_sentiment_response_model import DetectSentimentResponseModel
from src.data.models.error_response_model import ErrorResponseModel
from src.rnd.sentiment_analyzer import SentimentAnalysis
from typing import Union

class DetectSentimentUC:
    
    def __init__(self):
        self.sentiment_analysis = SentimentAnalysis()

    async def __call__(self, request_model: DetectSentimentRequestModel) -> Union[DetectSentimentResponseModel, ErrorResponseModel]:
        
        text = request_model.text
        
        try:
            # Perform sentiment analysis to get the sentiment label
            sentiment_label = self.sentiment_analysis.get_sentiment_from_text(text)
            # Create the response model with the sentiment label
            response_model = DetectSentimentResponseModel(sentiment=sentiment_label)
            return response_model
        
        #Error handling
        except Exception as e:
            print(e)
            error_message = "Sorry! The Service is currently unavailable. Please try again later."
            return ErrorResponseModel(error=error_message)
