# coding=utf-8

import json
import time
from hftcoin.mdagent.ccws import Exchange


class Bitstamp(Exchange):
    ExchangeId = 'Bitstamp'

    def collect_data(self):
        self.connect_redis()
        self.run_websocketapp(
            on_open=self.on_open,
        )

    def on_open(self, ws):
        ws.send(json.dumps(self.Config['Subscription']))
        self.Logger.info('Subscription')

    def process_order_data(self):
        input_key = self.Config['RedisCollectKey']
        output_key = self.Config['RedisOutputKey']
        pre_book = []
        while True:
            if self.RedisConnection.llen(input_key) < 1:
                time.sleep(60)
                continue
            [ct, msg] = json.loads(self.RedisConnection.rpop(input_key).decode('utf-8'))
            msg = json.loads(msg)
            if msg.get('event') != 'data':
                continue
            data = eval(msg['data'])
            ts = int(data['timestamp']) * 1000
            dt = self.fmt_date(ts)
            asks = [[float(i) for i in j] for j in data.get('asks')]
            bids = [[float(i) for i in j] for j in data.get('bids')]
            bids.sort(key=lambda x: x[0])
            asks.sort(key=lambda x: x[0])
            book = self._cut_order_book(bids, asks, self.Config['OrderBookDepth'])
            if book != pre_book:
                pre_book = book
                self.RedisConnection.lpush(output_key, json.dumps([ct, ts, dt] + book))

    def process_trade_data(self):
        input_key = self.Config['RedisCollectKey']
        output_key = self.Config['RedisOutputKey']
        while True:
            if self.RedisConnection.llen(input_key) < 1:
                time.sleep(60)
                continue
            [ct, msg] = json.loads(self.RedisConnection.rpop(input_key).decode('utf-8'))
            msg = json.loads(msg)
            if msg.get('event') != 'trade':
                continue
            data = eval(msg['data'])
            ts = int(data['timestamp']) * 1000
            dt = self.fmt_date(ts)
            self.RedisConnection.lpush(output_key, json.dumps([ct, ts, dt] + [data[i] for i in self.Config['Header']]))
