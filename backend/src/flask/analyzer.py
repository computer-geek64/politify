#!/usr/bin/python3 -B
# analyzer.py

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import openai
import psycopg2
from threading import Thread
from web.twitter import get_tweets
from ml.bert.train_test import get_predictions
import ml.google_cloud.nlp as google_cloud_nlp
from flask import Blueprint, request, jsonify
from config import DB_NAME, DB_USER, DB_PASSWORD, OPENAI_API_KEY


analyzer_blueprint = Blueprint('analyzer_blueprint', __name__, template_folder=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'templates'), static_folder=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'static'))


# New user submission
@analyzer_blueprint.route('/people/new/', methods=['POST'])
def post_new_person():
    if not request.is_json:
        return 'Invalid JSON request', 400
    username = request.get_json()['handle'].replace('@', '', 1)
    thread = Thread(target=analyze_person, args=(username,))
    thread.start()
    return 'Success', 200


@analyzer_blueprint.route('/analyze/', methods=['POST'])
def post_analyze_tweet():
    if not request.is_json:
        return 'Invalid JSON Request', 400
    tweet = request.get_json()['tweet']
    bert_prediction = get_predictions([tweet])[0]
    google_cloud_nlp_prediction = google_cloud_nlp.get_sentiment_predictions([tweet])[0]
    #openai_prediction = predict_openai(tweet)
    if google_cloud_nlp_prediction != 'non-political':
        return google_cloud_nlp_prediction.capitalize(), 200
    #elif openai_prediction not in ('left', 'right'):
    #    return openai_prediction.capitalize(), 200
    else:
        return bert_prediction.capitalize(), 200


def predict_openai(text):
    openai.api_key = OPENAI_API_KEY
    response = openai.Completion(engine='davinci', prompt='''Tweet: "I think women should be able to choose what they do with their bodies"
Sentiment: Left
###
Tweet: "The radical left or socialism is such a pain💢"
Sentiment: Right
###
Tweet: "Donald Trump is the best thing to happen to this country👍"
Sentiment: Right
###
Tweet: "This country needs to heal right now"
Sentiment: Left
###
Tweet: "This is the link to the article"
Sentiment: Neutral
###
Tweet: "I voted to acquit former President Trump. Read my full statement below"
Sentiment: Right
###
Tweet: "Now it’s time for us as a country to move on. We need to remember that at the end of the day we’re on the same team: the American team. Both sides can do better at remembering that."
Sentiment: Right
###
Tweet: "This trial proved Trump’s high crimes against the Constitution. 43 senators put Trump first and failed the test of history. But history was also made with the largest bipartisan majority ever voting to convict a president. The rest of the story is ours to write."
Sentiment: Left
###
Tweet: "Too many Republican senators are comfortable hiding behind their misguided belief that trying a former president for his actions in office is unconstitutional — even as they refuse to answer whether actually inciting an insurrection is unconstitutional."
Sentiment: Left
###
Tweet: "I voted for convicting Trump because he should be held accountable for inciting a violent insurrection against the will of the people, Congress, and our Democracy. He should be held accountable for violating his oath of office and failing to support and defend our Constitution."
Sentiment: Left
###
Tweet: "After carefully listening to every minute of the presentations made by the House Managers and the former president’s legal team, I am convinced that the Senate does not have jurisdiction to render a judgement against the former president. Therefore, I voted not guilty."
Sentiment: Right
###
Tweet: "I was proud to pay a high starting wage in my own business, but a national $15 minimum wage would be a straight jacket on the economy. You're going to lose somewhere around 1 to 1.5 million jobs, especially in places hit hardest by COVID like restaurants."
Sentiment: Right
###
Tweet: "REPORT: A $15 min wage would Upwards arrow child care costs 21% on avg in America. Child care costs in Iowa are already skyrocketing. A $15 min wage is not the right solution for our working families. Expanding access to child care is—& I'll keep fighting to do so."
Sentiment: Right
###
Tweet: "The CDC & overwhelming scientific data say it’s safe for kids to go back to school. Schools have only used $4B of the $68B they’ve already been given by Congress. So why is Biden ok with unions keeping kids out of the classroom schools closed?"
Sentiment: Right
###
Tweet: "The facts and the evidence were overwhelming—former President Donald Trump lied for months to his supporters, summoned them to Washington, and incited a violent insurrection against our government and our democracy."

Sentiment: Left
###
Tweet: "I saw and heard firsthand the insurrectionists, at the behest of the former president, try to use fear and violence to overturn our democratic election."
Sentiment: Left
###
Tweet: "It is truly sad and dangerous that only 7 Republicans voted to convict a president who is promoting a Big Lie, conspiracy theories and violence, and is aggressively trying to destroy American democracy."
Sentiment: Left
###
Tweet: "The evidence presented was overwhelming: Donald Trump used the presidency to incite a violent insurrection against our democracy. A bipartisan majority of Senators voted today to send a message to future presidents: this kind of conduct is impeachable and disqualifying."
Sentiment: Left
###
Tweet: "'THERE'S A LOT OF BUYER'S REMORSE' -- Sen. @MarshaBlackburn on the reaction she's seen from Americans to President Biden's flurry of executive orders"
Sentiment: Right
###
Tweet: "Environmental justice is about following the golden rule. I co-founded @EJusticeCaucus with @SenDuckworth and @SenBooker because we have a moral obligation to provide Americans with clean air to breathe and clean water to drink, regardless of race or zip code. It's time to act."
Sentiment: Left
###
Tweet: "This #BlackHistoryMonth, we honor the legacy of Hazel Johnson, the “Mother of Environmental Justice” by continuing to fight for bold, robust environmental legislation. Every American has the right to breathe clean air, drink safe water, & live on uncontaminated land."
Sentiment: Left
###
Tweet: "''' + text + '''"
Sentiment:''', max_tokens=3)
    print(response)
    return response['choices'][0]['text'].lower().replace('###', '').strip()


def analyze_person(username):
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    cursor = conn.cursor()

    cursor.execute('''
DELETE FROM person
      WHERE username = %s;
''', (username,))
    conn.commit()

    description = 'I am a politician.'

    print('[-] Scraping tweets...')
    name, picture, tweets = get_tweets(username, 200, True)
    print(f'[+] {len(tweets)} found!')

    print('[-] Predicting...')

    bert_predictions = get_predictions(tweets)
    google_cloud_nlp_predictions = google_cloud_nlp.get_sentiment_predictions(tweets)
    predictions = []

    for i in range(len(tweets)):
        if google_cloud_nlp_predictions[i] != 'non-political':
            predictions.append(google_cloud_nlp_predictions[i])
        else:
            predictions.append(bert_predictions[i])

    score = predictions.count('right') / len(tweets)

    print('[+] Prediction finished')

    cursor.execute('''
INSERT INTO person
            (
                username,
                name,
                description,
                picture,
                score
            )
     VALUES (
                %s,
                %s,
                %s,
                %s,
                %s
            );
''', (username, name, description, picture, score))

    params = []
    for tweet in tweets:
        params.append(username)
        params.append(tweet)

    cursor.execute('''
INSERT INTO tweet
            (
                username,
                tweet
            )
     VALUES ''' + ', '.join(['(%s, %s)'] * len(tweets)) + ';', tuple(params))
    conn.commit()
    conn.close()
