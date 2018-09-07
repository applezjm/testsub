# coding=utf-8

import json
import time
from hftcoin.mdagent.ccws import Exchange


class Bitfinex(Exchange):
    ExchangeId = 'Bitfinex'

    def collect_data(self):
        self.connect_redis()
        self.run_websocketapp(
            on_open=self.on_open,
        )

    def on_open(self, ws):
        ws.send(json.dumps(self.Config['Subscription']))
        self.Logger.info('Subscription')

    def process_order_book_data(self):
        input_key = self.Config['RedisCollectKey']
        output_key = self.Config['RedisOutputKey']
        is_initialized = False
        asks, bids = [], []
        book, book_pre = [], []
        init_book_len = self.Config['InitBookDepth']
        while True:
            if self.RedisConnection.llen(input_key) < 1:
                time.sleep(60)
                continue
            [ct, msg] = json.loads(self.RedisConnection.rpop(input_key).decode('utf-8'))
            msg = json.loads(msg)
            if type(msg) == dict:
                continue
            if len(msg[1]) == init_book_len * 2:
                data = msg[1]
                data = [[float(i), float(k)] for [i, _, k] in data]
                bids = data[0:init_book_len]
                bids.sort(key=lambda x: x[0])
                asks = data[init_book_len:2*init_book_len]
                asks = [[i, -j] for [i, j] in asks]
                asks.sort(key=lambda x: x[0])
                is_initialized = True
                book = self._cut_order_book(bids, asks, self.Config['OrderBookDepth'])
                ts = ct
                dt = self.fmt_date(ts)
                self.RedisConnection.lpush(output_key, json.dumps([ct, ts, dt] + book))
            elif is_initialized:
                data = msg[1]
                if data == 'hb':
                    continue
                side = 'bid' if float(data[2]) > 0 else 'ask'
                alias = eval('%ss' % side)
                if not alias:
                    if int(data[1]) != 0:
                        alias.append([float(data[0]), abs(float(data[2]))])
                else:
                    if int(data[1]) == 0:
                        self._update_order_book(bids, asks, side, float(data[0]), 0)
                    else:
                        self._update_order_book(bids, asks, side, float(data[0]), abs(float(data[2])))
                    book = self._cut_order_book(bids, asks, self.Config['OrderBookDepth'])
                if book == book_pre:
                    continue
                book_pre = book
                ts = ct
                dt = self.fmt_date(ts)
                if 'None' not in book:
                    self.RedisConnection.lpush(output_key, json.dumps([ct, ts, dt] + book))
            else:
                self.Logger.info(msg)

    def process_trade_data(self):
        input_key = self.Config['RedisCollectKey']
        output_key = self.Config['RedisOutputKey']
        is_initialized = False
        while True:
            if self.RedisConnection.llen(input_key) < 1:
                time.sleep(60)
                continue
            [ct, msg] = json.loads(self.RedisConnection.rpop(input_key).decode('utf-8'))
            msg = json.loads(msg)
            if type(msg) == dict:
                continue
            if type(msg[1]) is list:
                msg[1].reverse()
                data = msg[1]
                for ticker in data:
                    ts = int(ticker[1])
                    dt = self.fmt_date(ts)
                    side = 'bid' if float(ticker[2]) > 0 else 'ask'
                    data_output = ['init', ticker[0], side, abs(float(ticker[2])), ticker[3]]
                    self.RedisConnection.lpush(output_key, json.dumps([ct, ts, dt] + data_output))
                is_initialized = True
            elif is_initialized:
                ty = msg[1]
                if ty == 'hb':
                    continue
                else:
                    data = msg[2]
                    ts = int(data[1])
                    dt = self.fmt_date(ts)
                    side = 'bid' if float(data[2]) > 0 else 'ask'
                    data_output = [ty, data[0], side, abs(float(data[2])), data[3]]
                    self.RedisConnection.lpush(output_key, json.dumps([ct, ts, dt] + data_output))
            else:
                self.Logger.info(msg)



