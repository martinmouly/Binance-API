# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

import requests
import sqlite3
con = sqlite3.connect('tradingData1.db')
cur=con.cursor()

             
#%% list of all available cryptos on binance
def availableCryptos():
    url="https://api.binance.com/api/v3/ticker/price"
    r = requests.get(url)
    json_file=r.json()
    print("Available pairs on Binance")
    for elem in json_file:
        print((elem['symbol']))

#%% 
direction='bid'
pair='BTCUSD'
def getDepth(direction,pair):   
    url="https://api.binance.com/api/v3/ticker/bookTicker"
    pm={'symbol': pair}
    r=requests.get(url,params=pm)
    json_file=r.json()
    priceToShow=direction+"Price"
    print(json_file['symbol'])
    print(direction.upper(),":",json_file[priceToShow])

#%% order book 
def orderBook(pair):
    url="https://api.binance.com/api/v3/depth"
    pm={'symbol': pair}
    r=requests.get(url,params=pm)
    json_file=r.json()
    print(json_file)

def refreshDataCandle(pair,duration):
    tablename="BINANCE_"+pair+"_"+duration
    cur.execute(f'''CREATE TABLE IF NOT EXISTS {tablename}
               (date INT,
                open REAL,
                high REAL,
                low REAL,
                close REAL,
                volume REAL)''')
    url="https://api.binance.com/api/v3/klines"
    pm={'symbol': pair,'interval':duration,'limit':1}
    r=requests.get(url,params=pm)
    json_file=r.json()
    titles=['open time:','open:','high:','low:','close','volume:']
    for i in range(6):
        print(titles[i],json_file[0][i])
    query=f"INSERT INTO {tablename} VALUES ("+str(json_file[0][0])+","+str(json_file[0][1])+","+str(json_file[0][2])+","+str(json_file[0][3])+","+str(json_file[0][4])+","+str(json_file[0][5])+")"
    print(query)
    cur.execute(query)

#%% create and cancel orders
def createOrder(api_key,secret_key,direction,price,amount,pair,orderType):
    url="https://api.binance.com/api/v3/order"
    pm={'symbol': pair,'side':direction,'type':orderType,'price':price,'quantity':amount}
    r=requests.post(url,params=pm)
    json_file=r.json()
    print(json_file)

def cancelOrder(api_key,secret_key,uuid):
    url="https://api.binance.com/api/v3/order"
    pm={'symbol': uuid}
    r=requests.delete(url,params=pm)
    json_file=r.json()
    print(json_file)
#%% test functions
#availableCryptos()
pair='ETHBUSD'
direction='bid'
#getDepth(direction,pair)
#orderBook(pair)
duration='5m'
refreshDataCandle(pair,duration)

    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    