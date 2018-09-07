import csv
import ccxt


def get_okex_static(file):
    with open(file, 'a') as csvFile:
        csvwriter = csv.writer(csvFile)
        okex = ccxt.okex()
        for i in okex.fetch_markets():
            if i['symbol'] in ['BTC/USDT', 'ETH/USDT', 'BCH/USDT'] and i['info']['symbol']\
                    in ['btc_usdt', 'eth_usdt', 'bch_usdt']:
                uid = i['symbol'].replace('/', '_') + '-okex'
                csvwriter.writerow([uid, 'Okex', i['id'], i['info']['quoteIncrement'], '1',
                                    i['limits']['amount']['min'],
                                    i['limits']['amount']['max'], i['limits']['price']['min'],
                                    i['limits']['price']['max'], i['precision']['amount'],
                                    i['precision']['price'], i['taker'] * 10000,
                                    i['maker'] * 10000, 0, 0, 'cryptocurrency'])
