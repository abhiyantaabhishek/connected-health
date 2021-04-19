#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2019, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __license__ = "MIT"
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
import json
import time
import pandas as pd
from datetime import datetime
from flask import Flask, Response, render_template
import pickle
app = Flask(__name__)
#import requests

url = "https://luminous-fire-9722.firebaseio.com/Health.json/"

headers = {
    'application-id': "2AA28C7B-9C0E-99AB-FFF5-75156EC1FF00",
    'secret-key': "4EA6B2D9-C23B-A54D-FFC8-2E7B96623E00",
    'application-type': "REST",

    }


@app.route('/')
def index():
    return render_template('index.html')
	
@app.route('/data', methods=['GET', 'POST'])
def data():
	return render_template('data.html')
	
@app.route('/chart-data')
def chart_data():
    def generate_random_data():       
        file_in = open("data.pickle",'rb')
        data = pickle.load(file_in)
        json_data_server = list(data[range(0,2000,10)])
        file_in.close()          
        start = 0
        end = 200-1
        #responses = requests.request("GET", url, headers=headers)        
        #json_data_server = json.loads(responses.text)
        while True:
            if(start >= end):
                #json_data_server = new_json_data_server
                start = 0
            start = start+1
            json_data = json.dumps(
                #{'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': random.random() * 100})
                {'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': json_data_server[start]})
                #{'time': df['date_time'].iloc[ind], 'value': int(df['hr'].iloc[ind])}) 
                #{'time': df['date_time'].iloc[ind], 'value':  ind})                  
            yield f"data:{json_data}\n\n"
            time.sleep(0.1)

    return Response(generate_random_data(), mimetype='text/event-stream')


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
