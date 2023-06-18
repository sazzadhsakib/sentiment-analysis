from src.data.models.detect_sentiment_request_model import DetectSentimentRequestModel
from src.data.models.detect_sentiment_response_model import DetectSentimentResponseModel
from src.rnd.sentiment_analyzer import SentimentAnalysis

class DetectSentimentUC:
    def __init__(self):
        self.sentiment_analysis = SentimentAnalysis()

    async def __call__(self, request_model: DetectSentimentRequestModel) -> DetectSentimentResponseModel:
        text = request_model.text
        print(text)
        # Perform sentiment analysis to get the sentiment label
        sentiment_label =self.sentiment_analysis.get_sentiment_from_text(text)
        print(sentiment_label)
        # Create the response model with the sentiment label
        response_model = DetectSentimentResponseModel(sentiment=sentiment_label)

        return response_model
