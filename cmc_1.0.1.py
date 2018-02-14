#! python3
# cmc_1.0.0.py - coinmarketcap on CLI

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

        c = json.loads(response.text)
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

            window.addstr(i+2,0,rank)
            window.addstr(i+2,10,symbol)
            window.addstr(i+2,20,str(round(float(price_usd),3)))
            window.addstr(i+2,33,str(round(float(twofour_volume_usd))))
            window.addstr(i+2,50,str(round(float(marketcap))))
            window.addstr(i+2,65,str(round(float(total_supply))))
            if((percent_change_1h) == None):
                i = 0
            elif(float(percent_change_1h) < 0):
                window.addstr(i+2,80,percent_change_1h, curses.color_pair(197))
            else:
                window.addstr(i+2,80, "+" + percent_change_1h, curses.color_pair(47))
            if((percent_change_24h) == None):
                i = 0
            elif(float(percent_change_24h) < 0):
                window.addstr(i+2,90,percent_change_24h, curses.color_pair(197))
            else:
                window.addstr(i+2,90, "+" + percent_change_24h, curses.color_pair(47))
            if((percent_change_7d) == None):
                i = 0
            elif(float(percent_change_7d) < 0):
                window.addstr(i+2,102,percent_change_7d, curses.color_pair(197))
            else:
                window.addstr(i+2,102, "+" + percent_change_7d, curses.color_pair(47))

        window.refresh()
        time.sleep(0.5)


if len(sys.argv) < 2:
    print('Usage: coinmarketcap in CLI number of coins')
    sys.exit()
num = ' '.join(sys.argv[1:])

curses.wrapper(pbar)
