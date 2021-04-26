# Program Name : EOD.py
#
# Program Function : Ok, in class this week we learned about API calls
#                    Our lecturer was stepping through API calls to update GitHub
#                    I thought about doing it - but I live in dread of overwriting my homework so ..
#                    My 9 yr old has been asking about stocks (yes my eyes glazed over) so I thought I would see if there were APIs relating to the stock market
#                    I had intended writing the code today but I got side tracked helping someone through an IDR CA
#                    This is my placeholder note to myself to remind me what I planned o doing in programming to keep myself entertained
#
# Source API : https://marketstack.com
#

import requests

params = {
  'access_key': 'GOTTA_GET_AN_ACCESS_KEY'
}

api_result = requests.get('https://api.marketstack.com/v1/tickers/aapl/eod', params)

api_response = api_result.json()

for stock_data in api_response['data']:
    print(u'Ticker %s has a day high of  %s on %s' % (
      stock_data['symbol']
      stock_data['high']
      stock_data['date']
    ))ate']
))

