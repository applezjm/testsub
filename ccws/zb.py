# coding=utf-8

import json
import time
from hftcoin.mdagent.ccws import Exchange


class Zb(Exchange):
    ExchangeId = 'Zb'

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
            ts = int(msg.get('timestamp')) * 1000
            dt = self.fmt_date(ts)
            asks = [[float(i) for i in j] for j in msg.get('asks')]
            bids = [[float(i) for i in j] for j in msg.get('bids')]
            bids.sort(key=lambda x: x[0], reverse=True)
            asks.sort(key=lambda x: x[0])
            book = bids[0:self.Config['OrderBookDepth']] + asks[0:self.Config['OrderBookDepth']]
            book = sum(book, [])
            if pre_book == book:
                continue
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
            events = msg.get('data', [])
            for event in events:
                data = [event.get(k) for k in self.Config['Header']]
                ts = int(event.get('date')) * 1000
                dt = self.fmt_date(ts)
                self.RedisConnection.lpush(output_key, json.dumps([ct, ts, dt] + data))
