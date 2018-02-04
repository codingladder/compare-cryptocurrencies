# Noel Caceres
# Chart class for cryptoCompare


import matplotlib.pyplot as plt
from matplotlib.finance import date2num
from matplotlib.dates import MonthLocator, WeekdayLocator, DayLocator, HourLocator, DateFormatter, drange
import matplotlib.ticker as ticker
import numpy as np
import datetime


class Chart():
    # 2 coin name strings, 1 date list,  2 price lists , and 2 corresponding percentage lists
    def __init__(self, coin1, coin2, _dates, _prices1, _prices2, _percent1, _percent2):
        self.__dates = _dates
        self.__prices1 = _prices1
        self.__prices2 = _prices2
        self.__percent1 = _percent1
        self.__percent2 = _percent2
        
        # dates for x axis
        x = map(datetime.datetime.strptime, self.__dates, len(self.__dates)*['%b %d, %Y'])

        # prices and percentages for y axis
        y1 = np.array(map(float, self.__prices1))
        y2 = np.array(map(float, self.__prices2))
        percent1 = np.array(map(float, self.__percent1))
        percent2 = np.array(map(float, self.__percent2))

        # share x axis 
        f, axarr = plt.subplots(3, sharex=True)

        f.suptitle(coin1 + ' vs ' + coin2)
        axarr[0].plot(x, y1)
        axarr[1].plot(x, y2)
        axarr[2].plot(x,percent1,'g',label=coin1)
        axarr[2].plot(x,percent2,'m',label=coin2)
        axarr[2].legend(loc=2, prop={'size': 10})

        axarr[0].set_ylabel(coin1)
        axarr[1].set_ylabel(coin2)
        axarr[2].set_ylabel(" % ")

        axarr[0].yaxis.set_major_formatter(ticker.FormatStrFormatter('$%1.f'))
        axarr[1].yaxis.set_major_formatter(ticker.FormatStrFormatter('$%1.2f'))
        axarr[2].yaxis.set_major_formatter(ticker.FormatStrFormatter('%1.f')) 

        fig = plt.gcf()
        fig.canvas.set_window_title("Crypto Prices")
        ax = plt.gcf().axes[0]
        ax.xaxis.set_major_locator(WeekdayLocator())
        ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))

        plt.gcf().autofmt_xdate(rotation=45)
        
        plt.show()
    
             
