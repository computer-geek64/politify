#!/usr/bin/python3 -B
# nlp.py

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import re
from config import GOOGLE_APPLICATION_CREDENTIALS_LOCATION
from google.cloud import language_v1


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = GOOGLE_APPLICATION_CREDENTIALS_LOCATION
client = language_v1.LanguageServiceClient()


def preprocess_text(text):
    # Makes text lowercase
    # Removes hyperlinks
    # Replaces newlines with spaces
    # Removes trailing spaces
    return re.sub(r'https?:\/\/.*[\r\n]*', '', text.lower()).replace('\n', ' ').strip()


def get_sentiment_predictions(texts):
    predictions = []
    for text in texts:
        #text = preprocess_text(text)
        document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
        sentiments = client.analyze_sentiment(request={'document': document})
        score = 0
        for sentence in sentiments.sentences:
            for keyword in keywords:
                if keyword['phrase'].replace(' ', '') in sentence.text.content.lower().replace(' ', ''):
                    if sentence.sentiment.score <= -0.4:
                        if keyword['negative'] == 'left':
                            score -= keyword['priority']
                        else:
                            score += keyword['priority']
                    elif sentence.sentiment.score >= 0.4:
                        if keyword['positive'] == 'left':
                            score -= keyword['priority']
                        else:
                            score += keyword['priority']
                    break
        if score < 0:
            predictions.append('left')
        elif score > 0:
            predictions.append('right')
        else:
            predictions.append('non-political')
    return predictions


keywords = [
    {'phrase': 'biden', 'positive': 'left', 'negative': 'right', 'priority': 3},
    {'phrase': 'trump', 'positive': 'right', 'negative': 'left', 'priority': 3},
    {'phrase': 'maga', 'positive': 'right', 'negative': 'left', 'priority': 3},
    {'phrase': 'make america great again', 'positive': 'right', 'negative': 'left', 'priority': 3},
    {'phrase': 'prolife', 'positive': 'right', 'negative': 'left', 'priority': 3},
    {'phrase': 'pro-life', 'positive': 'right', 'negative': 'left', 'priority': 3},
    {'phrase': 'pro life', 'positive': 'right', 'negative': 'left', 'priority': 3},
    {'phrase': 'prochoice', 'positive': 'left', 'negative': 'right', 'priority': 3},
    {'phrase': 'pro-choice', 'positive': 'left', 'negative': 'right', 'priority': 3},
    {'phrase': 'antiabortion', 'positive': 'right', 'negative': 'left', 'priority': 3},
    {'phrase': 'anti-abortion', 'positive': 'right', 'negative': 'left', 'priority': 3},
    {'phrase': 'anti abortion', 'positive': 'right', 'negative': 'left', 'priority': 3},
    {'phrase': 'abortion', 'positive': 'left', 'negative': 'right', 'priority': 3},
    {'phrase': 'gun control', 'positive': 'left', 'negative': 'right', 'priority': 3},
    {'phrase': 'guns', 'positive': 'right', 'negative': 'left', 'priority': 3},
    {'phrase': '2nd amendment', 'positive': 'right', 'negative': 'left', 'priority': 3},
    {'phrase': 'second amendment', 'positive': 'right', 'negative': 'left', 'priority': 3},
    #{'phrase': 'economy', 'positive': 'right', 'negative': 'left', 'priority': 3},
    {'phrase': 'budget deficit', 'positive': 'left', 'negative': 'right', 'priority': 3},
    {'phrase': 'free healthcare', 'positive': 'left', 'negative': 'right', 'priority': 3},
    {'phrase': 'socialism', 'positive': 'left', 'negative': 'right', 'priority': 3},
    {'phrase': 'socialist', 'positive': 'left', 'negative': 'right', 'priority': 3},
    {'phrase': 'supreme court', 'positive': 'right', 'negative': 'left', 'priority': 2},
    {'phrase': 'foreign policy', 'positive': 'left', 'negative': 'right', 'priority': 3},
    {'phrase': 'antiimmigration', 'positive': 'right', 'negative': 'left', 'priority': 3},
    {'phrase': 'anti-immigration', 'positive': 'right', 'negative': 'left', 'priority': 3},
    {'phrase': 'anti immigration', 'positive': 'right', 'negative': 'left', 'priority': 3},
    {'phrase': 'immigration', 'positive': 'left', 'negative': 'right', 'priority': 3},
    {'phrase': 'racism', 'positive': 'right', 'negative': 'left', 'priority': 2},
    {'phrase': 'climate', 'positive': 'right', 'negative': 'left', 'priority': 3},
    {'phrase': 'global warming', 'positive': 'right', 'negative': 'left', 'priority': 3},
    {'phrase': 'coal', 'positive': 'right', 'negative': 'left', 'priority': 3},
    {'phrase': 'petroleum', 'positive': 'right', 'negative': 'left', 'priority': 3},
    {'phrase': 'mining', 'positive': 'right', 'negative': 'left', 'priority': 3},
    {'phrase': 'natural gas', 'positive': 'right', 'negative': 'left', 'priority': 3},
    {'phrase': 'domestic terrorism', 'positive': 'right', 'negative': 'left', 'priority': 3},
    {'phrase': 'steny hoyer', 'positive': 'left', 'negative': 'right', 'priority': 2},
    {'phrase': 'jim clyburn', 'positive': 'left', 'negative': 'right', 'priority': 2},
    {'phrase': 'katherine clark', 'positive': 'left', 'negative': 'right', 'priority': 2},
    {'phrase': 'hakeem jeffries', 'positive': 'left', 'negative': 'right', 'priority': 2},
    {'phrase': 'pete aguilar', 'positive': 'left', 'negative': 'right', 'priority': 2},
    {'phrase': 'sean patrick maloney', 'positive': 'left', 'negative': 'right', 'priority': 2},
    {'phrase': 'matt cartwright', 'positive': 'left', 'negative': 'right', 'priority': 2},
    {'phrase': 'debbie dingell', 'positive': 'left', 'negative': 'right', 'priority': 2},
    {'phrase': 'ted lieu', 'positive': 'left', 'negative': 'right', 'priority': 2},
    {'phrase': 'joe neguse', 'positive': 'left', 'negative': 'right', 'priority': 2},
    {'phrase': 'colin allred', 'positive': 'left', 'negative': 'right', 'priority': 2},
    {'phrase': 'mondaire jones', 'positive': 'left', 'negative': 'right', 'priority': 2},
    {'phrase': 'cheri bustos', 'positive': 'left', 'negative': 'right', 'priority': 2},
    {'phrase': 'barbara lee', 'positive': 'left', 'negative': 'right', 'priority': 2},
    {'phrase': 'eric swalwell', 'positive': 'left', 'negative': 'right', 'priority': 2},
    {'phrase': 'butterfield', 'positive': 'left', 'negative': 'right', 'priority': 2},
    {'phrase': 'jan schakowsky', 'positive': 'left', 'negative': 'right', 'priority': 2},
    {'phrase': 'steve scalise', 'positive': 'right', 'negative': 'left', 'priority': 2},
    {'phrase': 'liz cheney', 'positive': 'right', 'negative': 'left', 'priority': 2},
    {'phrase': 'mike johnson', 'positive': 'right', 'negative': 'left', 'priority': 2},
    {'phrase': 'rich hudson', 'positive': 'right', 'negative': 'left', 'priority': 2},
    {'phrase': 'gary palmer', 'positive': 'right', 'negative': 'left', 'priority': 2},
    {'phrase': 'tom emmer', 'positive': 'right', 'negative': 'left', 'priority': 2},
    {'phrase': 'drew ferguson', 'positive': 'right', 'negative': 'left', 'priority': 2},
    {'phrase': 'impeach', 'positive': 'left', 'negative': 'right', 'priority': 3},
    {'phrase': 'senate', 'positive': 'left', 'negative': 'right', 'priority': 2},
    {'phrase': 'stimulus', 'positive': 'left', 'negative': 'right', 'priority': 3},
    {'phrase': 'health insurance', 'positive': 'left', 'negative': 'right', 'priority': 3},
    {'phrase': 'social security', 'positive': 'left', 'negative': 'right', 'priority': 3}
]
