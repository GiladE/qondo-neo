from flask import request, jsonify, make_response
from app import app
from app.models import *

@app.route("/api/", methods=["GET"])
def api_index():
    data = { "PING": "PONG" }
    return make_response(jsonify(data), 200)

@app.route("/api/sentiments/", methods=["GET"])
def sentiments_index():
    data = { "PING": "PONG" }
    return make_response(jsonify(data), 200)

@app.route("/api/answers/<tweetid>", methods=["POST"])
def post_answer(tweetid):
    data = { "PING": "PONG" }
    return make_response(jsonify(data), 200)
