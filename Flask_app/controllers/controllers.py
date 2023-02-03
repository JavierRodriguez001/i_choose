from Flask_app import app
from flask import render_template, request, redirect, session, flash, jsonify
import os
from pprint import pprint
import requests
import random


@app.route('/')
def you_choose():
    # print('WHAT WE GOT FROM API --------------->', results.json())
    return render_template('index.html')


@app.route('/getresults', methods=["post"])
def get_results():
    session['form'] = request.form
    return redirect("/results")



@app.route('/results')
def restaurant_results():
    latLong = session['form']['location']
    category = session['form']['category']
    radius = session['form']['radius']
    print(latLong, category, radius)

    results = requests.get(f'https://api.content.tripadvisor.com/api/v1/location/nearby_search?latLong={latLong}&key={os.environ.get("TRIP_ADVISOR_API")}&category={category}&radius={radius}&radiusUnit=mi&language=en')

    ran_num = random.randint(0,9)
    print(ran_num)


    print(results.json())
    results = results.json()
    return render_template('results.html',results=results['data'], ran_num=ran_num)