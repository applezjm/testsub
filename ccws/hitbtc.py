# coding=utf-8

import json
import time
from hftcoin.mdagent.ccws import Exchange


class Hitbtc(Exchange):
    ExchangeId = 'Hitbtc'

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
        is_initialized = False
        book_pre = []
        asks, bids = [], []
        while True:
            if self.RedisConnection.llen(input_key) < 1:
                time.sleep(60)
                continue
            [ct, msg] = json.loads(self.RedisConnection.rpop(input_key).decode('utf-8'))
            ts = ct
            msg = json.loads(msg)
            if 'method' not in msg.keys():
                continue
            if msg['method'] == 'snapshotOrderbook':
                bids = [[float(i['price']), float(i['size'])] for i in msg['params']['bid']]
                bids.sort(key=lambda x: x[0])
                asks = [[float(i['price']), float(i['size'])] for i in msg['params']['ask']]
                asks.sort(key=lambda x: x[0])
                dt = self.fmt_date(ts)
                book = self._cut_order_book(bids, asks, self.Config['OrderBookDepth'])
                self.RedisConnection.lpush(output_key, json.dumps([ct, ts, dt] + book))
                is_initialized = True
            elif msg['method'] == 'updateOrderbook' and is_initialized:
                for pair in msg['params']['bid']:
                    self._update_order_book(bids, asks, 'bid',
                                            float(pair['price']), float(pair['size']))
                for pair in msg['params']['ask']:
                    self._update_order_book(bids, asks, 'ask',
                                            float(pair['price']), float(pair['size']))
                book = self._cut_order_book(bids, asks, self.Config['OrderBookDepth'])
                if book == book_pre:
                    continue
                book_pre = book
                dt = self.fmt_date(ts)
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
            if 'method' not in msg.keys():
                continue
            msg = msg['params']['data']
            for data in msg:
                ts = self.date_from_str(data.get('timestamp', '2010-01-01T00:00:01.000000Z'))
                dt = self.fmt_date(ts.timestamp() * 1000)
                ts = int(ts.timestamp() * 1000)
                self.RedisConnection.lpush(output_key, json.dumps([ct, ts, dt] +
                                                                  [data[i] for i in self.Config['Header']]))


