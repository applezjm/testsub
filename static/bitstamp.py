import csv
import ccxt


def get_bitstamp_static(file):
    bitstamp = ccxt.bitstamp()
    fee = bitstamp.fees
    taker_fee, maker_fee = fee['trading']['taker'], fee['trading']['maker']

    with open(file, 'a') as csvFile:
        csvwriter = csv.writer(csvFile)
        for i in bitstamp.fetch_markets():
            if i['symbol'] in ['BTC/USD', 'ETH/USD', 'BCH/USD']:
                uid = i['symbol'].replace('/', '_') + '-bitstamp'
                csvwriter.writerow([uid, 'Bitstamp', i['id'], '', '1',
                                    i['limits']['amount']['min'], i['limits']['amount']['max'],
                                    i['limits']['price']['min'], i['limits']['price']['max'],
                                    i['precision']['amount'], i['precision']['price'], taker_fee * 10000,
                                    maker_fee * 10000, 0, 0, 'cryptocurrency'])
