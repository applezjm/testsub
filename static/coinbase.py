import csv
import ccxt


def get_coinbase_static(file):
    with open(file, 'a') as csvFile:
        csvwriter = csv.writer(csvFile)
        coinbasepro = ccxt.coinbasepro()
        for i in coinbasepro.fetch_markets():
            if i['symbol'] in ['BTC/USD', 'ETH/USD', 'BCH/USD']:
                uid = i['symbol'].replace('/', '_') + '-gdax'
                csvwriter.writerow([uid, 'Coinbasepro', i['id'], i['info']['quote_increment'], '1',
                                    i['limits']['amount']['min'], i['limits']['amount']['max'],
                                    i['limits']['price']['min'], i['limits']['price']['max'],
                                    i['precision']['amount'], i['precision']['price'], i['taker'] * 10000,
                                    i['maker'] * 10000, 0, 0, 'cryptocurrency'])
