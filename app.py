from flask import Flask,jsonify
import pandas as pd
import numpy as np
import datetime
app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/linechart', methods=['GET'])
def line_data():
    df=pd.read_csv("Price_Volume_PurBid_SellBid_PurchaseVol_SellVol_For_Market_2 (1).csv")
    df["TimeStamp_date"]=int(datetime.datetime.timestamp(df["BlockStartTime"]))
    combine=df[["TimeStamp_date","MCPValues"]].values.tolist()
    output = {'results': combine}

    # return data
    return jsonify(results=output)
