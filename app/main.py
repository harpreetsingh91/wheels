#!/usr/bin/python
# -*- coding: utf-8 -*-
import bottle
import json
import heapq
import random
import copy
import os

###### server shit down here
@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


# code to give link for pictures and shit
@bottle.get('/')
def index():
    head_url = '%s://%s/static/head.jpg' \
        % (bottle.request.urlparts.scheme,
           bottle.request.urlparts.netloc)

    return {'color': '#00ff00', 'head': head_url}


@bottle.get('/test1')
def test1():
    return {'text': 'Hello WOrld'}

#lat is latidude
#lng is longitude
@bottle.get('/test2')
def test2():
    data = bottle.request.json
    return data


# Expose WSGI app (so gunicorn can find it)

application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'),
               port=os.getenv('PORT', '8080'))
