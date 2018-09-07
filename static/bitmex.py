import csv
import ccxt


def get_bitmex_static(file):
    with open(file, 'a') as csvFile:
        csvwriter = csv.writer(csvFile)
        bitmex = ccxt.bitmex()
        for i in bitmex.fetch_markets():
            if i['symbol'] in ['BTC/USD', 'ETH/USD']:
                uid = i['symbol'].replace('/', '_') + '-bitmex'
                csvwriter.writerow([uid, 'Bitmex', i['id'], i['info']['tickSize'], '1', i['limits']['amount']['min'],
                                    i['limits']['amount']['max'], i['limits']['price']['min'],
                                    i['limits']['price']['max'], i['precision']['amount'],
                                    i['precision']['price'], i['info']['takerFee'] * 10000,
                                    i['info']['makerFee'] * 10000, 0, 0, 'cryptocurrency'])
