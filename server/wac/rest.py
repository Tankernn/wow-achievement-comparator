#!/usr/bin/python3

from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin
from whoosh.qparser import MultifieldParser
from whoosh import index

from . import api

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

ix = index.open_dir("data")

@app.route("/search/<query>")
@cross_origin()
def search(query):
    with ix.searcher() as searcher:
        query = MultifieldParser(["title", "description"], ix.schema).parse(query)
        results = searcher.search(query, limit=10)
        return jsonify([dict(r) for r in results])

if __name__ == '__main__':
    app.run()
