# Noel Caceres
# Compare 2 cryptocurrencies
# by scraping coinmarketcap.com
# and plotting the comparison

from chart import *


# MAIN
if __name__ == '__main__':

    # 2 coins and start and end dates for comparison
    coin1 = 'bitcoin'   
    coin2 = 'monero'    
    start = '20171018'
    end = '20180203'

            
    # create chart with data
    myChart = Chart("Crypto Compare", coin1, coin2, start, end)
    #Chart(coin1, coin2, datesList, prices1, prices2, percent1, percent2)
    myChart.display()



    
    

    

    


