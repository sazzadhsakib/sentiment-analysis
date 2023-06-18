from setfit import SetFitModel

class SentimentAnalysis:

    def __init__(self):
        self.model = SetFitModel.from_pretrained("./output/", local_files_only=True)

    def map_sentiment_labels(self, sentiment_tensor):
        print(sentiment_tensor)
        labels = ["negative", "neutral", "happy"]
        sentiment_labels = [labels[i] for i in sentiment_tensor]
        return sentiment_labels

    def get_sentiment_from_text(self, ):
        text_list = [
            "Food is happiness",
            "Give me some sunshine"
            ""
        ]
        preds = self.model(text_list)
        analyzedLabels = self.map_sentiment_labels(preds)
        print(analyzedLabels)
        return analyzedLabels




