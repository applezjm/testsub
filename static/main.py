import os
import csv
import datetime
import time
import pytz
from static.hitbtc import get_hitbtc_static
from static.bitfinex import get_bitfinex_static
from static.gemini import get_gemini_static
from static.binance import get_binance_static
from static.bitmex import get_bitmex_static
from static.coinbase import get_coinbase_static
from static.huobipro import get_huobipro_static
from static.okex import get_okex_static
from static.bitstamp import get_bitstamp_static
from static.zb import get_zb_static


def create_csv():
    timezone = pytz.timezone('Asia/Shanghai')
    path = '/data/hftdata/CryptoExchanges/static/cryptocurrency'
    tmr = datetime.datetime.fromtimestamp(time.time(), timezone)
    filepath = '%s/%4d/%02d/%02d' % (path, tmr.year, tmr.month, tmr.day)
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    file = '%s/static_file.csv' % filepath
    if os.path.exists(file):
        os.remove(file)
    with open(file, 'a') as csvFile:
        csvwriter = csv.writer(csvFile)
        csvwriter.writerow(['uid', 'Exchange', 'Tradeable', 'TickSize', 'TradingUnit', 'LimitAmountMin',
                            'LimitAmountMax', 'LimitPriceMin', 'LimitPriceMax', 'PrecisionAmount',
                            'PrecisionPrice', 'TakerFeeInBasis', 'MakerFeeInBasis',
                            'TakerFeeInDollar', 'MakerFeeInDollar', 'Product'])
    return file


def main():
    file = create_csv()
    get_coinbase_static(file)
    get_gemini_static(file)
    get_bitmex_static(file)
    get_binance_static(file)
    get_okex_static(file)
    get_bitfinex_static(file)
    get_huobipro_static(file)
    get_hitbtc_static(file)
    get_bitstamp_static(file)
    get_zb_static(file)


if __name__ == '__main__':
    main()
