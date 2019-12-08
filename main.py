#!/usr/bin/env python
from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for
#from weather import query_api
from datetime import datetime
import os
import pytz
import requests
import math
API_KEY = '11697a88ce2c0b8893df209ea1becc86' 
API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}')






app = Flask(__name__)


def query_api(city):
    try:
        #print(API_URL.format(city, API_KEY))
        #data = requests.get(API_URL.format(city, API_KEY)).json()
        data = {"coord":{"lon":-0.13,"lat":51.51},"weather":[{"id":300,"main":"Drizzle","description":"light intensity drizzle","icon":"09d"}],"base":"stations","main":{"temp":280.32,"pressure":1012,"humidity":81,"temp_min":279.15,"temp_max":281.15},"visibility":10000,"wind":{"speed":4.1,"deg":80},"clouds":{"all":90},"dt":1485789600,"sys":{"type":1,"id":5091,"message":0.0103,"country":"GB","sunrise":1485762037,"sunset":1485794875},"id":2643743,"name":"London","cod":200}

    except Exception as exc:
        print(exc)
        data = None
    return data


@app.route('/')
def index():    
    return render_template('weather.html',        
                            data=[{'name':'Toronto'}, 
                                  {'name':'Montreal'}, 
                                  {'name':'Calgary'}])

@app.route("/result" , methods=['GET', 'POST'])
def result():
    data = []
    error = None
    select = request.form.get('comp_select')
    resp = query_api(select)
    pp(resp)
    if resp:
       data.append(resp)
    if len(data) != 2:
        error = 'Bad Response from Weather API'
    return render_template(
        'result.html',
        data=data,
        error=error)



if __name__=='__main__':
    app.run(debug=True)

