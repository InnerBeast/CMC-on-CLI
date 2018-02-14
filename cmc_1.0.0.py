#! python3
# quickWeather.py - Prints the weather for a location from the command line.

import json, requests, sys, pprint
import os
import time
import curses

def pbar(window):
    curses.start_color()
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)
    while True:
        url = 'https://api.coinmarketcap.com/v1/ticker/?limit=%s' % (num)
        response = requests.get(url)
        response.raise_for_status()
        # TODO: Load JSON data into a Python variable.
        c = json.loads(response.text)
        #window.addstr(0,0,"Hello")
        # Prints coin data.
        window.addstr(0,0,'Top %s coins:' % (num))
        window.addstr(1,0,'Rank')
        window.addstr(1,10,'Symbol')
        window.addstr(1,20,'Price:USD')
        window.addstr(1,33,'24Hr Volume:USD')
        window.addstr(1,50,'MarketCap:USD')
        window.addstr(1,65,'Total Supply')
        window.addstr(1,80,'% 1 Hour')
        window.addstr(1,90,'% 24 Hours')
        window.addstr(1,102,'% 7 Days')
        for i in range(int(num)):
            rank = c[i]['rank']
            symbol = c[i]['symbol']
            price_usd = c[i]['price_usd']
            twofour_volume_usd = c[i]['24h_volume_usd']
            marketcap = c[i]['market_cap_usd']
            total_supply = c[i]['total_supply']
            percent_change_1h = c[i]['percent_change_1h']
            percent_change_24h = c[i]['percent_change_24h']
            percent_change_7d = c[i]['percent_change_7d']
            #str(c[i]['rank'] + '    ' + c[i]['symbol'] + '|' + c[i]['price_usd'] + c[i]['24h_volume_usd'] + c[i]['total_supply'] + c[i]['max_supply']+c[i]['percent_change_1h']+ c[i]['percent_change_24h']+c[i]['percent_change_7d'])
            window.addstr(i+2,0,rank)
            window.addstr(i+2,10,symbol)
            window.addstr(i+2,20,str(round(float(price_usd),3)))
            window.addstr(i+2,33,str(round(float(twofour_volume_usd))))
            window.addstr(i+2,50,str(round(float(marketcap))))
            window.addstr(i+2,65,str(round(float(total_supply))))
            if(float(percent_change_1h) < 0):
                window.addstr(i+2,80,percent_change_1h, curses.color_pair(197))
            else:
                window.addstr(i+2,80, "+" + percent_change_1h, curses.color_pair(47))
            if(float(percent_change_24h) < 0):
                window.addstr(i+2,90,percent_change_24h, curses.color_pair(197))
            else:
                window.addstr(i+2,90, "+" + percent_change_24h, curses.color_pair(47))
            if(float(percent_change_7d) < 0):
                window.addstr(i+2,102,percent_change_7d, curses.color_pair(197))
            else:
                window.addstr(i+2,102, "+" + percent_change_7d, curses.color_pair(47))

        window.refresh()
        time.sleep(0.5)


# Compute location from command line arguments.

if len(sys.argv) < 2:
    print('Usage: coinmarketcap in CLI number of coins')
    sys.exit()
num = ' '.join(sys.argv[1:])

# TODO: Download the JSON data from OpenWeatherMap.org's API.
curses.wrapper(pbar)
