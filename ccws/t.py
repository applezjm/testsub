import requests
import datetime
import os
import csv

Tag = ["time_period_start", "time_period_end", "time_open", "time_close", "price_open", "price_high", "price_low",
       "price_close", "volume_traded", "trades_count"]
Symbol = ['COINBASE_SPOT_BTC_USD', 'COINBASE_SPOT_BCH_USD', 'COINBASE_SPOT_ETH_USD', 'GEMINI_SPOT_BTC_USD',
          'GEMINI_SPOT_ETH_USD', 'HUOBIPRO_SPOT_BTC_USDT', 'HUOBIPRO_SPOT_BCH_USDT', 'HUOBIPRO_SPOT_ETH_USDT',
          'BINANCE_SPOT_BTC_USDT', 'BINANCE_SPOT_BCH_USDT', 'BINANCE_SPOT_ETH_USDT', 'OKEX_SPOT_BTC_USDT',
          'OKEX_SPOT_BCH_USDT', 'OKEX_SPOT_ETH_USDT']

with open('/home/applezjm/tmp', 'r') as f:
    symbol = f.__next__().strip()
    time = f.__next__().strip()
a = 5
while a:
    a -= 1
    url = 'https://rest.coinapi.io/v1/ohlcv/%s/history?period_id=1MIN&time_start=%s' % (symbol, time)
    headers = {'X-CoinAPI-Key': '3183C26F-1112-4E2A-9F03-FC30EE6F2950'}
    response = requests.get(url, headers=headers)
    if response.status_code == 429:
        with open('/home/applezjm/tmp', 'w') as f:
            f.write(symbol)
            f.write(time)
        exit(0)
    data = eval(response.text)
    for i in data:
        tmr = datetime.datetime.strptime(i['time_period_start'], "%Y-%m-%dT%H:%M:%S.0000000Z")
        if tmr.year == 2018 and tmr.month == 8 and tmr.day == 28:
            time = '2000-01-01T00:00:00'
            symbol_tag = Symbol.index(symbol)
            if symbol_tag == len(Symbol) - 1:
                exit(0)
            else:
                symbol = Symbol[symbol_tag + 1]
                break
        filepath = '%s/%4d/%02d/%02d' % ('/home/applezjm', tmr.year, tmr.month, tmr.day)
        if not os.path.exists(filepath):
            os.makedirs(filepath)
        filename = '%s.csv' % symbol
        file = '%s/%s' % (filepath, filename)
        if not os.path.exists(file):
            with open(file, 'a') as csvFile:
                csvwriter = csv.writer(csvFile)
                csvwriter.writerow(Tag)
                csvwriter.writerow([i[tag] for tag in Tag])
        else:
            with open(file, 'a') as csvFile:
                csvwriter = csv.writer(csvFile)
                csvwriter.writerow([i[tag] for tag in Tag])
    time = datetime.datetime.strptime(time, "%Y-%m-%dT%H:%M:%S") + datetime.timedelta(minutes=100)
    time = str(time).replace(' ', 'T')



