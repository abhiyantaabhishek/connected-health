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


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chart-data')
def chart_data():
    def generate_random_data():
        df = pd.read_csv("data.csv")
        ind = 0		
        while True:

            if(ind == df.size-1):
                ind=0
            else:
                ind=ind+1
            json_data = json.dumps(
                #{'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': random.random() * 100})
                {'time': df['date_time'].iloc[ind], 'value': int(df['hr'].iloc[ind])}) 
                #{'time': df['date_time'].iloc[ind], 'value':  ind})  				
            yield f"data:{json_data}\n\n"
            time.sleep(0.1)

    return Response(generate_random_data(), mimetype='text/event-stream')




if __name__ == '__main__':
    app.run(debug=True, threaded=True)
