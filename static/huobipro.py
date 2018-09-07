import csv
import ccxt


def get_huobipro_static(file):
    with open(file, 'a') as csvFile:
        csvwriter = csv.writer(csvFile)
        huobipro = ccxt.huobipro()
        for i in huobipro.fetch_markets():
            if i['symbol'] in ['BTC/USDT', 'ETH/USDT', 'BCH/USDT']:
                uid = i['symbol'].replace('/', '_') + '-huobipro'
                csvwriter.writerow([uid, 'Huobipro', i['id'], '0.01', '1', i['limits']['amount']['min'],
                                    i['limits']['amount']['max'], i['limits']['price']['min'],
                                    i['limits']['price']['max'], i['precision']['amount'],
                                    i['precision']['price'], i['taker'] * 10000, i['maker'] * 10000,
                                    0, 0, 'cryptocurrency'])
