# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests

def availableCryptos():
    url="https://api.binance.com/api/v3/ticker/price"
    r = requests.get(url)
    json_file=r.json()
    print("Available pairs on Binance")
    for elem in json_file:
        print((elem['symbol']))

#availableCryptos()
    
pair="MATICBTC"
direction="bid"
def getDepth(direction,pair):   
    url="https://api.binance.com/api/v3/ticker/bookTicker"
    pm={'symbol': pair}
    r=requests.get(url,params=pm)
    json_file=r.json()
    priceToShow=direction+"Price"
    print(json_file['symbol'])
    print(direction.upper(),":",json_file[priceToShow])

#getDepth(direction,pair)
pair="MATICBTC"
def orderBook(pair):
    url="https://api.binance.com/api/v3/depth"
    pm={'symbol': pair}
    r=requests.get(url,params=pm)
    json_file=r.json()
    print(json_file)
    
orderBook(pair)