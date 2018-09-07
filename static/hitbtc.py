import csv
import ccxt


def get_hitbtc_static(file):
    with open(file, 'a') as csvFile:
        csvwriter = csv.writer(csvFile)
        hitbtc = ccxt.hitbtc2()
        for i in hitbtc.fetch_markets():
            if i['symbol'] in ['BTC/USDT', 'ETH/USDT', 'BCH/USDT']:
                uid = i['symbol'].replace('/', '_') + '-hitbtc'
                csvwriter.writerow([uid, 'Hitbtc', i['id'], i['info']['tickSize'], '1', i['limits']['amount']['min'],
                                    i['limits']['amount']['max'], i['limits']['price']['min'],
                                    i['limits']['price']['max'], i['precision']['amount'],
                                    i['precision']['price'], i['taker'] * 10000, i['maker'] * 10000,
                                    0, 0, 'cryptocurrency'])
