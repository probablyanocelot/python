# https://youtu.be/XRA1jI7jx5k?t=653
import getreddit
from dataclasses import dataclass
from producer import publish

from flask import Flask, jsonify, make_response, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://test:test@db/reddiget'
CORS(app)

db = SQLAlchemy(app)


@dataclass
class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    url = db.Column(db.String(1000))


# MAKE THIS GET THE REDDIT PLAYLIST
@app.route('/api/reddit/<subreddit>')
def get_reddit(subreddit):
    data = getreddit.get_data('submission', subreddit, 200)
    data = getreddit.filter_data(data, criteria='youtu')
    return data


@app.route('/api/songs')
def index():
    return jsonify(Song.query.all())


INFO = {
    "colors": {
        "r": "red",
        "g": "green",
        "b": "blue",
    },
    "langs": {
        "es": "Spanish",
        "en": "English",
        "fr": "French",
    }
}


@app.route('/qstr')
def query_string():
    if request.args:
        req = request.args
        res = {}
        for key, value in req.items():
            res[key] = value
        res = make_response(jsonify(res), 200)
        return res

    res = make_response(jsonify({"error": "No query string"}, 400))
    return res


@app.route('/json')
def get_json():
    res = make_response(jsonify(INFO), 200)
    return res


@app.route('/json/<collection>/<member>')
def get_data(collection, member):
    if collection in INFO:
        member = INFO[collection].get(member)
        if member:
            res = make_response(jsonify({"res": member}), 200)
            return res

        res = make_response(jsonify({"error": "Member not found"}), 400)
        return res

    res = make_response(jsonify({"error": "Collection not found"}), 400)
    return res


@app.route('/json/<collection>', methods=['POST'])
def create_collection(collection):
    req = request.get_json()

    if collection in INFO:
        res = make_response(
            jsonify({"error": "Collection already exists"}), 400)
        return res

    INFO.update({collection: req})

    res = make_response(jsonify({'message': 'Collection created'}), 201)
    return res


@app.route('/')
def home():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
