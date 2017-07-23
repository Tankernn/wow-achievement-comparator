#!/usr/bin/python3

from flask import Flask
from flask import jsonify
from whoosh.qparser import MultifieldParser
from whoosh import index

from . import api

app = Flask(__name__)

ix = index.open_dir("data")

@app.route("/search/<query>")
def search(query):
    with ix.searcher() as searcher:
        query = MultifieldParser(["title", "description"], ix.schema).parse(query)
        results = searcher.search(query, limit=10)
        return jsonify([dict(r) for r in results])

if __name__ == '__main__':
    app.run()
