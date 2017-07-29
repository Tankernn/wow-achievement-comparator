#!/usr/bin/python3

import toml
import requests

try:
    config = toml.load("config/default.toml")
except IOError as e:
    print(
        "No config file found. Please copy config/example.toml to "
        "config/default.toml and add your Blizzard API key. If you "
        "don't have one yet, you can register for one here: "
        "https://dev.battle.net/"
    )
    raise e

def get_json(method, **kwargs):
    params = dict(config['api'])
    params['method'] = method
    params.update(kwargs)
    r = requests.get("{url}{method}?locale={locale}&apiKey={key}".format(**params))
    return r.json()
