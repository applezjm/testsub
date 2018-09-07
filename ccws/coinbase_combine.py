import gzip
import csv
import math
import argparse
import datetime
import os
import subprocess


def differ(l1, l2):
    for i in range(len(l1)):
        if (i % 2 == 1 and abs(l2[i] - l1[i]) > 1e-8) or (i % 2 == 0 and abs(l2[i] - l1[i]) > 0.01):
            if i % 2 == 1 and (l2[i] - l1[i]) > 1e-8:
                if i < len(l1) / 2:
                    return l1[i - 1], l2[i] - l1[i], 0
                else:
                    return l1[i - 1], l2[i] - l1[i], 1
            elif i % 2 == 0 and i < len(l1)/2 and (l2[i] - l1[i]) > 0.01:
                    return l2[i], l2[i + 1], 0
            elif i % 2 == 0 and i >= len(l1)/2 and (l1[i] - l2[i]) > 0.01:
                    return l2[i], l2[i + 1], 1
            else:
                return 0, 0, 0
    return 0, 0, 0


def combine(y, m, d, ex):
    f1_book = '/data/hftdata/CryptoExchanges/market/%4d/%02d/%02d/%s-gdax.book.csv.gz' % (y, m, d, ex)
    f1_trade = '/data/hftdata/CryptoExchanges/market/%4d/%02d/%02d/%s-gdax.ticker.csv.gz' % (y, m, d, ex)
    f2_folder = '/data/hftdata/CryptoExchanges/processed_market/%4d/%02d/%02d' % (y, m, d)
    f2 = '/data/hftdata/CryptoExchanges/processed_market/%4d/%02d/%02d/%s-gdax.combine.csv.gz' % (y, m, d, ex)
    if not (os.path.exists(f1_book) and os.path.exists(f1_trade)):
        return
    if not os.path.exists(f2_folder):
        os.makedirs(f2_folder)
    time = 0
    head = sum([['bidp%d' % i, 'bidv%d' % i] for i in range(12)], []) +\
           sum([['askp%d' % i, 'askv%d' % i] for i in range(12)], [])
    initial = True
    not_finished = True
    last_book = []
    last_time = []
    last_trade_bid_size, last_trade_bid_price, last_trade_ask_size, last_trade_ask_price = [], [], [], []
    last_add_bid_size, last_add_bid_price, last_add_ask_size, last_add_ask_price = [], [], [], []

    with gzip.open(f1_book, 'rt') as fn1, gzip.open(f1_trade, 'rt') as fn3, open(f2, 'w+') as fn2:
        csvreader1 = csv.DictReader(fn1)
        csvreader2 = csv.DictReader(fn3)
        csvwriter = csv.writer(fn2)
        csvwriter.writerow(['reporttimestamp', 'timestamp', 'datetime'] +
                           head + ['bid_trade', 'bid_trade_price', 'ask_trade', 'ask_trade_price', 'bid_add',
                                   'bid_add_price', 'ask_add', 'ask_add_price'])
        while not_finished:
            if initial:
                row1 = csvreader1.__next__()
                row2 = csvreader2.__next__()
                time = math.ceil(float(row1['reporttimestamp']) / 1000) * 1000
                last_time = [row1[i] for i in ['reporttimestamp', 'timestamp', 'datetime']]
                last_book = [float(row1[i]) for i in head]
                row1 = csvreader1.__next__()
                initial = False
            else:
                while time >= int(row2['reporttimestamp']):
                    if row2['side'] == 'buy':
                        last_trade_bid_size.append(str(row2['last_size']))
                        last_trade_bid_price.append(str(row2['price']))
                    else:
                        last_trade_ask_size.append(str(row2['last_size']))
                        last_trade_ask_price.append(str(row2['price']))
                    try:
                        row2 = csvreader2.__next__()
                    except StopIteration:
                        not_finished = False
                        break
                while time >= int(row1['reporttimestamp']):
                    book = [float(row1[i]) for i in head]
                    price, size, side = differ(last_book, book)
                    if price != 0:
                        if side == 0:
                            last_add_bid_size.append(str(size))
                            last_add_bid_price.append(str(price))
                        else:
                            last_add_ask_size.append(str(size))
                            last_add_ask_price.append(str(price))
                    time = math.ceil(float(row1['reporttimestamp']) / 1000) * 1000
                    last_time = [row1[i] for i in ['reporttimestamp', 'timestamp', 'datetime']]
                    last_book = [float(row1[i]) for i in head]
                    try:
                        row1 = csvreader1.__next__()
                    except StopIteration:
                        not_finished = False
                        break
                csvwriter.writerow(last_time + last_book +
                                   ['|'.join(last_trade_bid_size), '|'.join(last_trade_bid_price),
                                    '|'.join(last_trade_ask_size), '|'.join(last_trade_ask_price),
                                    '|'.join(last_add_bid_size), '|'.join(last_add_bid_price),
                                    '|'.join(last_add_ask_size), '|'.join(last_add_ask_price)])

                time = math.ceil(float(row1['reporttimestamp']) / 1000) * 1000
                last_time = [row1[i] for i in ['reporttimestamp', 'timestamp', 'datetime']]
                last_book = [float(row1[i]) for i in head]
                row1 = csvreader1.__next__()

                last_trade_ask_price, last_trade_ask_size, last_trade_bid_price, last_trade_bid_size = [], [], [], []
                last_add_bid_size, last_add_bid_price, last_add_ask_size, last_add_ask_price = [], [], [], []
    subprocess.call('gzip %s' % f2, shell=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--start', metavar='start', required=True)
    parser.add_argument('-e', '--end', metavar='end', required=True)
    parser.add_argument('-E', '--exchange', metavar='exchange', required=True)
    args = parser.parse_args()

    start, end, ex = args.start, args.end, args.exchange
    start = datetime.datetime.strptime(start, '%Y/%m/%d')
    end = datetime.datetime.strptime(end, '%Y/%m/%d') + datetime.timedelta(days=1)
    while start != end:
        combine(start.year, start.month, start.day, ex)
        start += datetime.timedelta(days=1)


if __name__ == '__main__':
    main()

