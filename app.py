from flask import Flask,jsonify
import pandas as pd
import numpy as np
import datetime
app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/linechart_MCP')
def line_data_MCP():
    df=pd.read_csv("Price_Volume_PurBid_SellBid_PurchaseVol_SellVol_For_Market_2 (1).csv")
    df["BlockStartTime"]=pd.to_datetime(df["BlockStartTime"])
    df=df.rename(columns={"BlockStartTime":"x","MCPValues":"y"})
    combine=df[["x","y"]].to_json(orient="records")

    # return data
    return combine

@app.route('/linechart_Purchase')
def line_data_Purchase():
    df=pd.read_csv("Price_Volume_PurBid_SellBid_PurchaseVol_SellVol_For_Market_2 (1).csv")
    df["BlockStartTime"]=pd.to_datetime(df["BlockStartTime"])
    df=df.rename(columns={"BlockStartTime":"x","PurchaseBidValues":"y"})
    combine=df[["x","y"]].to_json(orient="records")

    # return data
    return combine

@app.route('/linechart_Sell')
def line_data_Sell():
    df=pd.read_csv("Price_Volume_PurBid_SellBid_PurchaseVol_SellVol_For_Market_2 (1).csv")
    df["BlockStartTime"]=pd.to_datetime(df["BlockStartTime"])
    df=df.rename(columns={"BlockStartTime":"x","SellBidValues":"y"})
    combine=df[["x","y"]].to_json(orient="records")

    # return data
    return combine

@app.route('/linechart_MCV')
def line_data_MCV():
    df=pd.read_csv("Price_Volume_PurBid_SellBid_PurchaseVol_SellVol_For_Market_2 (1).csv")
    df["BlockStartTime"]=pd.to_datetime(df["BlockStartTime"])
    df=df.rename(columns={"BlockStartTime":"x","MCVValues":"y"})
    combine=df[["x","y"]].to_json(orient="records")

    # return data
    return combine

# app.run(host="0.0.0.0",debug=True)