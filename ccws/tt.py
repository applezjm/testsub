import csv
import ccxt

exchange = ['binance', 'okex', 'huobipro', 'bithumb', 'bitfinex', 'hitbtc', 'zb', 'bibox',
            'lbank', 'dobi', 'bcex', 'digifinex', 'upbit', 'coinsuper', 'coinbasepro', 'kraken',
            'simex', 'oex', 'gateio', 'crypton', 'idcm', 'bittrex', 'coinbene', 'allcoin'
            'btcbox', 'coinsbank', 'kryptono', 'uex', 'exrates', 'bitstamp', 'bitflyer', 'bitbank',
            'sistemcoin', 'coinegg', 'poloniex', 'dragonex', 'fatbtc', 'yobit', 'rightbtc',
            'cointiger', 'bitlish', 'hotbit', 'c2cx', 'latoken', 'b2bx', 'bitmart', 'bitinka',
            'livecoin', 'kucoin', 'idax']
e = []
with open('/home/applezjm/fee.csv', 'w+') as fn:
    f = csv.writer(fn)
    f.writerow(['exchange', 'maker', 'taker'])
    for j in exchange:
        try:
            a = eval('ccxt.%s()' % j).fees
            f.writerow([j, a['trading']['maker'], a['trading']['taker']])
        except:
            f.writerow([j])
