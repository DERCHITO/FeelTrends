from google.cloud import language_v1
from typing import Dict

def analyze_sentiment(text: str) -> Dict:
    client = language_v1.LanguageServiceClient()
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    response = client.analyze_sentiment(request={'document': document})

    sentiment = response.document_sentiment
    return {
        "score": sentiment.score,
        "magnitude": sentiment.magnitude
    }
