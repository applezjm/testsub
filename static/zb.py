import csv
import ccxt


def get_zb_static(file):
    zb = ccxt.zb()
    fee = zb.fees
    taker_fee, maker_fee = fee['trading']['taker'], fee['trading']['maker']

    with open(file, 'a') as csvFile:
        csvwriter = csv.writer(csvFile)
        for i in zb.fetch_markets():
            if i['symbol'] in ['BTC/USDT', 'ETH/USDT', 'BCH/USDT']:
                uid = i['symbol'].replace('/', '_') + '-zb'
                csvwriter.writerow([uid, 'Zb', i['id'], '', '1', i['limits']['amount']['min'],
                                    i['limits']['amount']['max'], i['limits']['price']['min'],
                                    i['limits']['price']['max'], i['precision']['amount'],
                                    i['precision']['price'], taker_fee * 10000, maker_fee * 10000,
                                    0, 0, 'cryptocurrency'])
