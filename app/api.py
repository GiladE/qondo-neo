from flask import jsonify, make_response
from app import app

@app.route("/api/", methods=["ANY"])
def api_index():
    data = { "PING": "PONG" }
    return make_response(jsonify(data), 200)
