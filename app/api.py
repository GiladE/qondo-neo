from flask import request, jsonify, make_response
from app import app
from app.models import *

@app.route("/api/", methods=["GET"])
def api_index():
    data = { "PING": "PONG" }
    return make_response(jsonify(data), 200)

@app.route("/api/sentiments/", methods=["GET"])
def sentiments_index():
    tweet = Tweet.query.filter(~Tweet.answers.any()).first()

    if tweet != None:
        data = { "id": tweet.id, "text": tweet.text }
        return make_response(jsonify(data), 200)
    else:
        data = { "id": None, "text": None }
        return make_response(jsonify(data), 200)

@app.route("/api/answers/<tweetid>", methods=["POST"])
def post_answer(tweetid):
    tweet = Tweet.query.filter_by(id=tweetid).first()
    answer = Answer(tweet, SentimentType[request.json['sentiment']])

    db.session.add(answer)
    db.session.commit()

    tweet = Tweet.query.filter(~Tweet.answers.any()).first()

    if tweet != None:
        data = { "id": tweet.id, "text": tweet.text }
        return make_response(jsonify(data), 200)
    else:
        data = { "id": None, "text": None }
        return make_response(jsonify(data), 200)
