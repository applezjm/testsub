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


def combine(y, m, d):
    f1 = '/data/hftdata/CryptoExchanges/market/%4d/%02d/%02d/BTC_USD-gemini.book.csv.gz' % (y, m, d)
    f2_folder = '/data/hftdata/CryptoExchanges/processed_market/%4d/%02d/%02d' % (y, m, d)
    f2 = '/data/hftdata/CryptoExchanges/processed_market/%4d/%02d/%02d/BTC_USD-gemini.book.csv' % (y, m, d)
    if not os.path.exists(f1):
        return
    if not os.path.exists(f2_folder):
        os.makedirs(f2_folder)
    time = 0
    head = sum([['bidp%d' % i, 'bidv%d' % i] for i in range(12)], []) \
               + sum([['askp%d' % i, 'askv%d' % i] for i in range(12)], [])
    initial = True
    last_book = []
    last_time = []
    last_trade_tid = 0
    last_trade_bid_size, last_trade_bid_price, last_trade_ask_size, last_trade_ask_price = [], [], [], []
    last_add_bid_size, last_add_bid_price, last_add_ask_size, last_add_ask_price = [], [], [], []

    with gzip.open(f1, 'rt') as fn1, open(f2, 'w+') as fn2:
        csvreader = csv.DictReader(fn1)
        csvwriter = csv.writer(fn2)
        csvwriter.writerow(['reporttimestamp', 'timestamp', 'datetime'] +
                           head + ['bid_trade', 'bid_trade_price', 'ask_trade', 'ask_trade_price', 'bid_add',
                                   'bid_add_price', 'ask_add', 'ask_add_price'])
        for row in csvreader:
            book = [float(row[i]) for i in head]
            if not initial:
                if int(row['reporttimestamp']) >= time:
                    csvwriter.writerow(last_time +
                                       last_book + ['|'.join(last_trade_bid_size), '|'.join(last_trade_bid_price),
                                                    '|'.join(last_trade_ask_size), '|'.join(last_trade_ask_price),
                                                    '|'.join(last_add_bid_size), '|'.join(last_add_bid_price),
                                                    '|'.join(last_add_ask_size), '|'.join(last_add_ask_price)])
                    last_trade_ask_price, last_trade_ask_size, last_trade_bid_price, last_trade_bid_size = [], [], [], []
                    last_add_bid_size, last_add_bid_price, last_add_ask_size, last_add_ask_price = [], [], [], []

                price, size, side = differ(last_book, book)
                if price != 0:
                    if side == 0:
                        last_add_bid_size.append(str(size))
                        last_add_bid_price.append(str(price))
                    else:
                        last_add_ask_size.append(str(size))
                        last_add_ask_price.append(str(price))
            initial = False
            time = math.ceil(float(row['reporttimestamp']) / 1000) * 1000
            last_time = [row[i] for i in ['reporttimestamp', 'timestamp', 'datetime']]
            last_book = [float(row[i]) for i in head]
            if row['tid'] and row['tid'] != last_trade_tid:
                last_trade_tid = row['tid']
                if row['makerSide'] == 'bid':
                    last_trade_bid_size.append(str(row['amount']))
                    last_trade_bid_price.append(str(row['price']))
                else:
                    last_trade_ask_size.append(str(row['amount']))
                    last_trade_ask_price.append(str(row['price']))
    subprocess.call('gzip %s' % f2, shell=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--start', metavar='start', required=True)
    parser.add_argument('-e', '--end', metavar='end', required=True)
    args = parser.parse_args()

    start, end = args.start, args.end
    start = datetime.datetime.strptime(start, '%Y/%m/%d')
    end = datetime.datetime.strptime(end, '%Y/%m/%d') + datetime.timedelta(days=1)
    while start != end:
        combine(start.year, start.month, start.day)
        start += datetime.timedelta(days=1)


if __name__ == '__main__':
    main()



