#!/usr/bin/python3 -B
# nlp.py

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from config import GOOGLE_APPLICATION_CREDENTIALS_LOCATION
from google.cloud import language_v1


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = GOOGLE_APPLICATION_CREDENTIALS_LOCATION
client = language_v1.LanguageServiceClient()


def get_sentiment_prediction(texts):
    for text in texts:
        document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
        sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment


keywords = [
    {'phrase': 'biden', 'positive': 'left', 'negative': 'right', 'priority': 'high'},
    {'phrase': 'turmp', 'positive': 'right', 'negative': 'left', 'priority': 'high'},
    {'phrase': 'maga', 'positive': 'right', 'negative': 'left', 'priority': 'high'},
    {'phrase': 'prolife', 'positive': 'right', 'negative': 'left', 'priority': 'high'},
    {'phrase': 'pro-life', 'positive': 'right', 'negative': 'left', 'priority': 'high'},
    {'phrase': 'pro life', 'positive': 'right', 'negative': 'left', 'priority': 'high'},
    {'phrase': 'antiabortion', 'positive': 'right', 'negative': 'left', 'priority': 'high'},
    {'phrase': 'anti-abortion', 'positive': 'right', 'negative': 'left', 'priority': 'high'},
    {'phrase': 'anti abortion', 'positive': 'right', 'negative': 'left', 'priority': 'high'},
    {'phrase': 'abortion', 'positive': 'left', 'negative': 'right', 'priority': 'high'},
    {'phrase': 'gun control', 'positive': 'left', 'negative': 'right', 'priority': 'high'},
    {'phrase': 'guns', 'positive': 'right', 'negative': 'left', 'priority': 'high'},
    {'phrase': '2nd amendment', 'positive': 'right', 'negative': 'left', 'priority': 'high'},
    {'phrase': 'second amendment', 'positive': 'right', 'negative': 'left', 'priority': 'high'},
    #{'phrase': 'economy', 'positive': 'right', 'negative': 'left', 'priority': 'high'},
    {'phrase': 'budget deficit', 'positive': 'left', 'negative': 'right', 'priority': 'high'},
    {'phrase': 'free healthcare', 'positive': 'left', 'negative': 'right', 'priority': 'high'},
    {'phrase': 'socialism', 'positive': 'left', 'negative': 'right', 'priority': 'high'},
    {'phrase': 'socialist', 'positive': 'left', 'negative': 'right', 'priority': 'high'},
    {'phrase': 'supreme court', 'positive': 'right', 'negative': 'left', 'priority': 'medium'},
    {'phrase': 'foreign policy', 'positive': 'left', 'negative': 'right', 'priority': 'high'},
    {'phrase': 'antiimmigration', 'positive': 'right', 'negative': 'left', 'priority': 'high'},
    {'phrase': 'anti-immigration', 'positive': 'right', 'negative': 'left', 'priority': 'high'},
    {'phrase': 'anti immigration', 'positive': 'right', 'negative': 'left', 'priority': 'high'},
    {'phrase': 'immigration', 'positive': 'left', 'negative': 'right', 'priority': 'high'},
    {'phrase': 'racism', 'positive': 'right', 'negative': 'left', 'priority': 'medium'},
    {'phrase': 'climate', 'positive': 'right', 'negative': 'left', 'priority': 'high'},
    {'phrase': 'global warming', 'positive': 'right', 'negative': 'left', 'priority': 'high'},
    {'phrase': '', 'positive': '', 'negative': '', 'priority': ''},
    {'phrase': '', 'positive': '', 'negative': '', 'priority': ''},
    {'phrase': '', 'positive': '', 'negative': '', 'priority': ''},
    {'phrase': '', 'positive': '', 'negative': '', 'priority': ''},
    {'phrase': '', 'positive': '', 'negative': '', 'priority': ''},
    {'phrase': '', 'positive': '', 'negative': '', 'priority': ''},
    {'phrase': '', 'positive': '', 'negative': '', 'priority': ''},
    {'phrase': '', 'positive': '', 'negative': '', 'priority': ''},
    {'phrase': '', 'positive': '', 'negative': '', 'priority': ''},
    {'phrase': '', 'positive': '', 'negative': '', 'priority': ''},
    {'phrase': '', 'positive': '', 'negative': '', 'priority': ''},
    {'phrase': '', 'positive': '', 'negative': '', 'priority': ''},
    {'phrase': '', 'positive': '', 'negative': '', 'priority': ''},
    {'phrase': '', 'positive': '', 'negative': '', 'priority': ''},
    {'phrase': '', 'positive': '', 'negative': '', 'priority': ''},
    {'phrase': '', 'positive': '', 'negative': '', 'priority': ''},
    {'phrase': '', 'positive': '', 'negative': '', 'priority': ''},
    {'phrase': '', 'positive': '', 'negative': '', 'priority': ''},
]
