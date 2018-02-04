# Noel Caceres
# Compare 2 cryptocurrencies
# by scraping coinmarketcap.com
# and plotting the comparison

import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
import datetime
from matplotlib.finance import date2num
import numpy as np
import chart

# MAIN
if __name__ == '__main__':

    # 2 coins and start and end dates for comparison
    coin1 = 'bitcoin'   
    coin2 = 'monero'    
    start = '20171018'
    end = '20180118'

    # setup 2 web links to scrape for data
    page1 = 'https://coinmarketcap.com/currencies/' + coin1 \
        + '/historical-data/?start=' + start + '&end=' + end
    page2 = 'https://coinmarketcap.com/currencies/' + coin2 \
        + '/historical-data/?start=' + start + '&end=' + end

    # scrape data using BeautifulSoup 
    res1 = requests.get(page1)
    res2 = requests.get(page2)
    soup1 = BeautifulSoup(res1.content,'lxml')
    soup2 = BeautifulSoup(res2.content,'lxml')
    table1 = soup1.find_all('table')[0]
    table2 = soup2.find_all('table')[0]
    df1 = pd.read_html(str(table1))
    df2 = pd.read_html(str(table2))
    my_json1 = df1[0].to_json(orient='records')
    my_json2 = df2[0].to_json(orient='records')
    parsed1 = json.loads(my_json1)
    parsed2 = json.loads(my_json2)

    datesList = []
    prices1 = []
    prices2 = []
    percent1 = []
    percent2 = []
    # first price: use to calculate running percentage
    startingP1 = float(parsed1[len(parsed1)-1]['Close'])
    startingP2 = float(parsed2[len(parsed2)-1]['Close'])
    # reversed range loop to place data into lists
    for i in range(len(parsed1)-1,-1,-1):
        datesList.append(parsed1[i]['Date'])    # date into list
        tmpFloat = float(parsed1[i]['Close'])   # coin1 price
        prices1.append(tmpFloat)                # into prices2 list
        percent1.append(((tmpFloat / startingP1) - 1)*100) # coin1 percentage
        tmpFloat = float(parsed2[i]['Close'])   # coin2 price
        prices2.append(tmpFloat)                # into prices2 list
        percent2.append(((tmpFloat / startingP2) - 1)*100) # coin2 percentage
    # create chart with data
    chart.Chart(coin1, coin2, datesList, prices1, prices2, percent1, percent2)

    
    

    

    


