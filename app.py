from flask import Flask,jsonify
import pandas as pd
import numpy as np
import datetime
app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/linechart')
def line_data():
    df=pd.read_csv("Price_Volume_PurBid_SellBid_PurchaseVol_SellVol_For_Market_2 (1).csv")
    df["BlockStartTime"]=pd.to_datetime(df["BlockStartTime"])
    df["TimeStamp_date"]=df["BlockStartTime"].astype('int64')
    combine=df[["TimeStamp_date","MCPValues"]].values.tolist()

    # return data
    return jsonify(results=combine)

app.run(host="0.0.0.0",debug=True)