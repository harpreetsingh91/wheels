#!/usr/bin/python
# -*- coding: utf-8 -*-
import bottle
import json
import heapq
import random
import copy
import os
import googlemaps

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
@bottle.post('/test2')
def test2():
    data = bottle.request.json
    #data is in a dictionary
    returnedData = {}
    returnedData['lat'] = data["test1"]
    returnedData['lng'] = data["test2"]
    return returnedData

gmaps = googlemaps.Client(key = 'AIzaSyDEtK4FuvEMBByZ5c5EQCQ1UF3weG0ysM8')

@bottle.get('/testmap')
def testMap():
    #response.content_type = 'application/json'
    directions_result = gmaps.directions("UVic Bus Loop, Victoria, BC V8P 5C2", "2230 Edgelow St, Victoria, BC V8N 1R5", mode = "transit", alternatives = 'true')
    return {'response': [directions_result]}



# Expose WSGI app (so gunicorn can find it)

application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'),
               port=os.getenv('PORT', '8080'))
