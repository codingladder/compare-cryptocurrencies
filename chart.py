# Noel Caceres
# Chart class for cryptoCompare


import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
import datetime
import matplotlib.pyplot as plt
from matplotlib.finance import date2num
from matplotlib.dates import MonthLocator, WeekdayLocator, DayLocator, HourLocator, DateFormatter, drange
import matplotlib.ticker as ticker
import numpy as np


class Chart():
    def __init__(self, title, coin1, coin2, start, end):
        self.__title = title
        self.__coin1 = coin1
        self.__coin2 = coin2
        self.__start = start
        self.__end = end
        # setup 2 web links to scrape for data
        self.__page1 = 'https://coinmarketcap.com/currencies/' + self.__coin1 \
            + '/historical-data/?start=' + self.__start + '&end=' + self.__end
        self.__page2 = 'https://coinmarketcap.com/currencies/' + self.__coin2 \
            + '/historical-data/?start=' + self.__start + '&end=' + self.__end
        
    def display(self):

        # scrape data using BeautifulSoup 
        res1 = requests.get(self.__page1)
        res2 = requests.get(self.__page2)
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

        ##########
        
        # dates for x axis
        x = map(datetime.datetime.strptime, datesList, len(datesList)*['%b %d, %Y'])

        # prices and percentages for y axis
        y1 = np.array(map(float, prices1))
        y2 = np.array(map(float, prices2))
        percent1 = np.array(map(float, percent1))
        percent2 = np.array(map(float, percent2))

        # share x axis 
        f, axarr = plt.subplots(3, sharex=True)

        f.suptitle(self.__coin1 + ' vs ' + self.__coin2)
        axarr[0].plot(x, y1)
        axarr[1].plot(x, y2)
        axarr[2].plot(x,percent1,'g',label=self.__coin1)
        axarr[2].plot(x,percent2,'m',label=self.__coin2)
        axarr[2].legend(loc=2, prop={'size': 10})

        axarr[0].set_ylabel(self.__coin1)
        axarr[1].set_ylabel(self.__coin2)
        axarr[2].set_ylabel(" % ")

        axarr[0].yaxis.set_major_formatter(ticker.FormatStrFormatter('$%1.f'))
        axarr[1].yaxis.set_major_formatter(ticker.FormatStrFormatter('$%1.2f'))
        axarr[2].yaxis.set_major_formatter(ticker.FormatStrFormatter('%1.f')) 

        fig = plt.gcf()
        fig.canvas.set_window_title(self.__title)
        ax = plt.gcf().axes[0]
        ax.xaxis.set_major_locator(WeekdayLocator())
        ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))

        plt.gcf().autofmt_xdate(rotation=45)
        
        plt.show()
    
             
