from flask import Flask,jsonify,request
import pandas as pd
import numpy as np
import datetime
app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello_world():
    return 'Hello, World!'

# @app.route('/linechart_MCP')
# def line_data_MCP():
#     df=pd.read_csv("Price_Volume_PurBid_SellBid_PurchaseVol_SellVol_For_Market_2 (1).csv")
#     df["BlockStartTime"]=pd.to_datetime(df["BlockStartTime"])
#     df=df.rename(columns={"BlockStartTime":"x","MCPValues":"y"})
#     combine=df[["x","y"]].to_json(orient="records")

#     # return data
#     return combine

# @app.route('/linechart_Purchase')
# def line_data_Purchase():
#     df=pd.read_csv("Price_Volume_PurBid_SellBid_PurchaseVol_SellVol_For_Market_2 (1).csv")
#     df["BlockStartTime"]=pd.to_datetime(df["BlockStartTime"])
#     df=df.rename(columns={"BlockStartTime":"x","PurchaseBidValues":"y"})
#     combine=df[["x","y"]].to_json(orient="records")

#     # return data
#     return combine

# @app.route('/linechart_Sell')
# def line_data_Sell():
#     df=pd.read_csv("Price_Volume_PurBid_SellBid_PurchaseVol_SellVol_For_Market_2 (1).csv")
#     df["BlockStartTime"]=pd.to_datetime(df["BlockStartTime"])
#     df=df.rename(columns={"BlockStartTime":"x","SellBidValues":"y"})
#     combine=df[["x","y"]].to_json(orient="records")

#     # return data
#     return combine

# @app.route('/linechart_MCV')
# def line_data_MCV():
#     df=pd.read_csv("Price_Volume_PurBid_SellBid_PurchaseVol_SellVol_For_Market_2 (1).csv")
#     df["BlockStartTime"]=pd.to_datetime(df["BlockStartTime"])
#     df=df.rename(columns={"BlockStartTime":"x","MCVValues":"y"})
#     combine=df[["x","y"]].to_json(orient="records")

#     # return data
#     return combine

@app.route('/areaprice', methods=['GET'])
def search():
    day = request.args.get('day')
    month = request.args.get('month')
    year = request.args.get('year')
    value = request.args.get('value')
    input = f"{year}/{month}/{day}"

    format = '%Y/%m/%d'

    date = datetime.datetime.strptime(input, format)
    df=pd.read_csv("Price_Volume_PurBid_SellBid_PurchaseVol_SellVol_For_Market_2 (1).csv")
    df["BlockStartTime"]=pd.to_datetime(df["BlockStartTime"])

    new_df=df[df["Date"] == str(date.date())]
    new_df.replace(-1,np.nan,inplace=True)
    new_df=new_df.dropna()
    combine=new_df[['BlockStartTime',value]].to_json(orient="records")
    maxBlock=new_df[new_df[value]==new_df[value].max()]["BlockNumber"]
    max=new_df[value].max()
    minBlock=new_df[new_df[value]==new_df[value].min()]["BlockNumber"]
    min=new_df[value].min()
    mean=new_df[value].mean()
    median=new_df[value].median()
    json={
        'maxBlock':maxBlock.to_list(),
        'max':max,
        'minBlock':minBlock.to_list(),
        'min':min,
        'mean':mean,
        'median':median,
        'combine':combine
    }

    return json

# app.run(host="0.0.0.0",debug=True)