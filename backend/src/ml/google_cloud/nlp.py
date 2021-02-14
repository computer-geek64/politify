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
    {'phrase': 'coal', 'positive': 'right', 'negative': 'left', 'priority': 'high'},
    {'phrase': 'petroleum', 'positive': 'right', 'negative': 'left', 'priority': 'high'},
    {'phrase': 'mining', 'positive': 'right', 'negative': 'left', 'priority': 'high'},
    {'phrase': 'natural gas', 'positive': 'right', 'negative': 'left', 'priority': 'high'},
    {'phrase': 'domestic terrorism', 'positive': 'right', 'negative': 'left', 'priority': 'high'},
    {'phrase': 'steny hoyer', 'positive': 'left', 'negative': 'right', 'priority': 'low'},
    {'phrase': 'jim clyburn', 'positive': 'left', 'negative': 'right', 'priority': 'low'},
    {'phrase': 'katherine clark', 'positive': 'left', 'negative': 'right', 'priority': 'low'},
    {'phrase': 'hakeem jeffries', 'positive': 'left', 'negative': 'right', 'priority': 'low'},
    {'phrase': 'pete aguilar', 'positive': 'left', 'negative': 'right', 'priority': 'low'},
    {'phrase': 'sean patrick maloney', 'positive': 'left', 'negative': 'right', 'priority': 'low'},
    {'phrase': 'matt cartwright', 'positive': 'left', 'negative': 'right', 'priority': 'low'},
    {'phrase': 'debbie dingell', 'positive': 'left', 'negative': 'right', 'priority': 'low'},
    {'phrase': 'ted lieu', 'positive': 'left', 'negative': 'right', 'priority': 'low'},
    {'phrase': 'joe neguse', 'positive': 'left', 'negative': 'right', 'priority': 'low'},
    {'phrase': 'colin allred', 'positive': 'left', 'negative': 'right', 'priority': 'low'},
    {'phrase': 'mondaire jones', 'positive': 'left', 'negative': 'right', 'priority': 'low'},
    {'phrase': 'cheri bustos', 'positive': 'left', 'negative': 'right', 'priority': 'low'},
    {'phrase': 'barbara lee', 'positive': 'left', 'negative': 'right', 'priority': 'low'},
    {'phrase': 'eric swalwell', 'positive': 'left', 'negative': 'right', 'priority': 'low'},
    {'phrase': 'butterfield', 'positive': 'left', 'negative': 'right', 'priority': 'low'},
    {'phrase': 'jan schakowsky', 'positive': 'left', 'negative': 'right', 'priority': 'low'},
    {'phrase': 'steve scalise', 'positive': 'right', 'negative': 'left', 'priority': 'low'},
    {'phrase': 'liz cheney', 'positive': 'right', 'negative': 'left', 'priority': 'low'},
    {'phrase': 'mike johnson', 'positive': 'right', 'negative': 'left', 'priority': 'low'},
    {'phrase': 'rich hudson', 'positive': 'right', 'negative': 'left', 'priority': 'low'},
    {'phrase': 'gary palmer', 'positive': 'right', 'negative': 'left', 'priority': 'low'},
    {'phrase': 'tom emmer', 'positive': 'right', 'negative': 'left', 'priority': 'low'},
    {'phrase': 'drew ferguson', 'positive': 'right', 'negative': 'left', 'priority': 'low'},
    {'phrase': 'impeach', 'positive': 'left', 'negative': 'right', 'priority': 'high'},
    {'phrase': 'senate', 'positive': 'left', 'negative': 'right', 'priority': 'low'},
    {'phrase': 'stimulus', 'positive': 'left', 'negative': 'right', 'priority': 'high'},
    {'phrase': 'health insurance', 'positive': 'left', 'negative': 'right', 'priority': 'high'},
    {'phrase': 'social security', 'positive': 'left', 'negative': 'right', 'priority': 'high'}
]
