from setfit import SetFitModel

class SentimentAnalysis:

    def __init__(self):
        self.model = SetFitModel.from_pretrained("/home/sazzad/Documents/sazzad/personal/sentiment-analysis/src/rnd/output", local_files_only=True)

    def map_sentiment_labels(self, sentiment_tensor):
        print(sentiment_tensor)
        labels = ["negative", "neutral", "happy"]
        sentiment_label = labels[sentiment_tensor]
        return sentiment_label


    def get_sentiment_from_text(self, text):
        preds = self.model([text])
        analyzedLabels = self.map_sentiment_labels(preds)
        print(analyzedLabels)
        return analyzedLabels




