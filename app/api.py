from flask import request, jsonify, make_response
from sqlalchemy import create_engine
import pandas as pd
from app import app
from app.models import *

@app.route("/api/", methods=["GET"])
def api_index():
  data = { "PING": "PONG" }
  return make_response(jsonify(data), 200)

@app.route("/api/tweets/", methods=["GET"])
def tweets_index():
  tweet = Tweet.query.filter(~Tweet.answers.any()).first()

  if tweet != None:
    data = { "id": tweet.id, "text": tweet.text }
    return make_response(jsonify(data), 200)
  else:
    data = { "id": None, "text": None }
    return make_response(jsonify(data), 200)

@app.route("/api/tweets/", methods=["POST"])
def tweets_post():
  if 'file' not in request.files:
    data = { "error": "error" }
    return make_response(jsonify(data), 400)
  file = request.files['file']
  if file.filename == '':
    data = { "error": "error" }
    return make_response(jsonify(data), 400)
  if file and allowed_file(file.filename):
    data = pd.read_csv(file)

    engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
    data = data.rename(columns={'ItemID': 'externalid', 'SentimentText': 'text'})
    data.to_sql('tweets', engine, if_exists='append', index=False)
    data = { "success": "success" }
    return make_response(jsonify(data), 201)

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

def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in ["csv"]
