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
# Sigh, that was short lived .. I can't get the data over HTTPS without paying a fee
#
# New Source : RapidAPI. 
#              Yay! The call for Tesla data worked. Since I'm only allowed 500 free calls a month I've recorded the output data in a txt file and I'll use that to play around
#              and develop my wee program.
#              The plan :
#                  We're interested in a finite set of symbols since we are dealing with two restrictions - my son's attention span and the upper limit of 500 calls a month
#                  So I'm thinking .. I'll ultimately store the data in a database with one table summarising the symbols being imported and a table for each symbol storing the 
#                  historical data - the idea finally being we can show plots for given timeframes for given symbols - but obviously that is not happening today!

import requests

# Probably going to need these further down the line 
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib import rcParams

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/auto-complete"

querystring = {"q":"tesla","region":"US"}

headers = {
    'x-rapidapi-key': "Register",
    'x-rapidapi-host': "Register"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)




