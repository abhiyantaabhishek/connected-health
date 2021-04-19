#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2019, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __license__ = "MIT"
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
import json
import random
import time
from datetime import datetime
import pandas as pd
from flask import Flask, Response, render_template,make_response

app = Flask(__name__)
random.seed()  # Initialize the random number generator
import requests

url = "https://luminous-fire-9722.firebaseio.com/Health.json/"

headers = {
    'application-id': "2AA28C7B-9C0E-99AB-FFF5-75156EC1FF00",
    'secret-key': "4EA6B2D9-C23B-A54D-FFC8-2E7B96623E00",
    'application-type': "REST",

    }
import threading
import time


#class MyThread(threading.Thread):
#    def run(self): 
#        global go
#        global start 
#        global end 
#        global new_json_data_server
#    # Default called function with mythread.start()
#        print("{} started!".format(self.getName()))        # "Thread-x started!"
#        while True:
#            if(start >= end/2 and go ==1):
#                print("getting response")
#                response = requests.request("GET", url, headers=headers)
#                new_json_data_server = json.loads(response.text)
#                go = 0
#        
#        time.sleep(1)                                      # Pretend to work for a second
#        print("{} finished!".format(self.getName()))       # "Thread-x finished!"
#

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chart-data')
def chart_data():
    def generate_random_data():
        #df = pd.read_csv("data.csv")
        
        global go
        global start 
        global end 
        global new_json_data_server
        start = 0 
        print("getting response in cahrt_data")
        response = requests.request("GET", url, headers=headers)
        #json_data_server = new_json_data_server = json.loads(response.text)
        json_data_server = json.loads(response.text)
        print("starting while loop")
        while True:
            if(start >= end):
                #json_data_server = new_json_data_server
                start = 0
                go = 1
            start = start+1
            #if(ind == len(json_data_server)-1):
            #    ind=0
            #else:
            #    ind=ind+1
            json_data = json.dumps(
                {'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': json_data_server[start]})
                #{'time': df['date_time'].iloc[ind], 'value': int(df['hr'].iloc[ind])}) 
                     
            #print(json_data)                
            yield f"data:{json_data}\n\n"
            time.sleep(0.001)
    return Response(generate_random_data(), mimetype='text/event-stream')




if __name__ == '__main__':
    start = 0
    end =200-1
    new_json_data_server = [0]
    go = 1
    #mythread = MyThread(name = "Thread-{}".format(1))  # ...Instantiate a thread and pass a unique ID to it
    #mythread.start() 
    app.run(debug=True, threaded=True)
