# Download stock quotes in CSV


import requests
import time

i = 0

# obtain quote once every 3 seconds for the next 6 seconds
while (i < 2):

    # define the base url
    base_url = 'https://query1.finance.yahoo.com/v7/finance/quote'

    # retrieve data from web server
    data = requests.get(
        base_url,
        params={'formatted': 'true',
                'crumb': 'ibvjN1cjxSs',
                'lang': 'en-US',
                'region': 'US',
                'symbols': 'GOOG',
                'fields': 'messageBoardId,longName,shortName,marketCap,underlyingSymbol,underlyingExchangeSymbol,headSymbolAsString,regularMarketPrice,regularMarketChange,regularMarketChangePercent,regularMarketVolume,uuid,regularMarketOpen,fiftyTwoWeekLow,fiftyTwoWeekHigh,toCurrency,fromCurrency,toExchange,fromExchange',
                'corsDomain': 'finance.yahoo.com'
        }
    )

    # write the data to csv
    with open('stocks.csv', 'wb') as code:
        code.write(data.content)

    i += 1

    # pause for 3 seconds
    time.sleep(3)