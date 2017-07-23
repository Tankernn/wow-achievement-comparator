#!/usr/bin/python3

import os

from whoosh import index
from whoosh.fields import TEXT, NUMERIC, ID, Schema

from . import api

# Init whoosh
schema = Schema(title=TEXT(stored=True), id=NUMERIC(stored=True), icon=ID(stored=True), description=TEXT)
if not os.path.exists("data"):
    os.mkdir("data")
ix = index.create_in("data", schema)
writer = ix.writer()
# Get achievements
categories = api.get_json("/wow/data/character/achievements")['achievements']
def find_achievements(categories):
    for category in categories:
        if 'categories' in category:
            find_achievements(category['categories'])
        for achievement in category['achievements']:
            achi_data = {k: v for k, v in achievement.items() if k in ('description', 'icon', 'id', 'title')}
            writer.add_document(**achi_data)

find_achievements(categories)

writer.commit()
