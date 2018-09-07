import csv
from requests_html import HTMLSession
import ccxt


def get_binance_static(file):
    binance = ccxt.binance()
    fee = binance.fees
    taker_fee, maker_fee = fee['trading']['taker'], fee['trading']['maker']

    session = HTMLSession()
    url = 'https://support.binance.com/hc/en-us/articles/115000594711-Trading-Rule'
    r = session.get(url)
    text = r.html.text
    symbols = ['BTC/USDT', 'ETH/USDT', 'BCC/USDT']
    min_price = dict()
    for symbol in symbols:
        start = text.find(symbol)
        tmp = text[start:].split('\n')
        if symbol == 'BCC/USDT':
            symbol = 'BCH/USDT'
        min_price[symbol] = tmp[3]

    with open(file, 'a') as csvFile:
        csvwriter = csv.writer(csvFile)
        for i in binance.fetch_markets():
            if i['symbol'] in ['BTC/USDT', 'ETH/USDT', 'BCH/USDT']:
                uid = i['symbol'].replace('/', '_') + '-binance'
                csvwriter.writerow([uid, 'Binance', i['id'], i['info']['filters'][0]['tickSize'], '1',
                                    i['limits']['amount']['min'],
                                    i['limits']['amount']['max'], min_price[i['symbol']],
                                    '', i['precision']['amount'],
                                    i['precision']['price'], taker_fee * 10000, maker_fee * 10000,
                                    0, 0, 'cryptocurrency'])
