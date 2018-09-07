# coding=utf-8

import json
import time
from hftcoin.mdagent.ccws import Exchange


class Gdax(Exchange):
    ExchangeId = 'Gdax'

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
        initiate = False
        asks, bids = [], []
        book_pre = []
        while True:
            if self.RedisConnection.llen(input_key) < 1:
                time.sleep(60)
                continue
            [ct, msg] = json.loads(self.RedisConnection.rpop(input_key).decode('utf-8'))
            msg = json.loads(msg)
            ts, dt, ty = ct, '', msg.get('type', None)
            if ty == 'snapshot':
                bids = [[float(i) for i in j] for j in msg.get('bids')]
                bids.sort(key=lambda x: x[0])
                asks = [[float(i) for i in j] for j in msg.get('asks')]
                asks.sort(key=lambda x: x[0])
                dt = self.fmt_date(ts)
                ty = 'Y'
                initiate = True
                book = self._cut_order_book(bids, asks, self.Config['OrderBookDepth'])
                self.RedisConnection.lpush(output_key, json.dumps([ct, ts, dt, ty] + book))
            elif initiate and ty == 'l2update':
                changes = msg.get('changes', [])
                for change in changes:
                    self._update_order_book(bids, asks, change[0], float(change[1]), float(change[2]))
                book = self._cut_order_book(bids, asks, self.Config['OrderBookDepth'])
                if book == book_pre:
                    continue
                book_pre = book
                ts = self.date_from_str(msg.get('time', '2010-01-01T00:00:01.000000Z'))
                dt = self.fmt_date(ts.timestamp() * 1000)
                ts = int(ts.timestamp() * 1000)
                ty = 'N'
                self.RedisConnection.lpush(output_key, json.dumps([ct, ts, dt, ty] + book))
            else:
                #self.Logger.info(msg)
                pass

    def process_ticker_data(self):
        input_key = self.Config['RedisCollectKey']
        output_key = self.Config['RedisOutputKey']
        initiate = False
        while True:
            if self.RedisConnection.llen(input_key) < 1:
                time.sleep(60)
                continue
            [ct, msg] = json.loads(self.RedisConnection.rpop(input_key).decode('utf-8'))
            msg = json.loads(msg)
            ts, dt, ty = ct, '', msg.get('type', None)
            if ty == 'subscriptions':
                initiate = True
                continue
            elif initiate:
                data = [msg.get(k) for k in self.Config['Header']]
                ts = self.date_from_str(msg.get('time', '2010-01-01T00:00:01.000000Z'))
                if int(ts.timestamp()) == 1262304001 and msg.get('trade_id', None) is None:
                    continue
                dt = self.fmt_date(ts.timestamp() * 1000)
                ts = int(ts.timestamp() * 1000)
                self.RedisConnection.lpush(output_key, json.dumps([ct, ts, dt] + data))

    def process_order_book_update_info(self):
        input_key = self.Config['RedisCollectKey']
        output_key = self.Config['RedisOutputKey']
        initiate = False
        last_ts = 0
        last_data = []
        while True:
            if self.RedisConnection.llen(input_key) < 1:
                time.sleep(60)
                continue
            [ct, msg] = json.loads(self.RedisConnection.rpop(input_key).decode('utf-8'))
            msg = json.loads(msg)
            ts, ty = self.date_from_str(msg.get('time', '2010-01-01T00:00:01.000000Z')), msg.get('type')
            # need to be del
            initiate = True
            if ty == 'subscriptions':
                initiate = True
                continue
            elif initiate and ty == 'open':
                side = 0 if msg['side'] == 'buy' else 1
                data = [float(msg['price']), float(msg['remaining_size']), side, 1]

                if ts == last_ts and last_data[3] == 1 and data[0] == last_data[0] and data[2] == last_data[2]:
                    data[1] += last_data[1]
                else:
                    if last_ts:
                        dt = self.fmt_date(last_ts.timestamp() * 1000)
                        last_ts = int(last_ts.timestamp() * 1000)
                        self.RedisConnection.lpush(output_key, json.dumps([ct, last_ts, dt] + last_data))
                last_ts = ts
                last_data = data
            elif initiate and ty == 'done' and msg.get('reason', None) == 'canceled':
                if last_ts:
                    dt = self.fmt_date(last_ts.timestamp() * 1000)
                    last_ts = int(last_ts.timestamp() * 1000)
                    self.RedisConnection.lpush(output_key, json.dumps([ct, last_ts, dt] + last_data))

                last_ts = ts
                side = 0 if msg['side'] == 'buy' else 1
                last_data = [float(msg['price']), float(msg['remaining_size']), side, 2]
            elif initiate and ty == 'match':
                side = 0 if msg['side'] == 'buy' else 1
                data = [float(msg['price']), float(msg['size']), side, 0]

                if ts == last_ts and last_data[3] == 0 and data[0] == last_data[0] and data[2] == last_data[2]:
                    data[1] += last_data[1]
                else:
                    if last_ts:
                        dt = self.fmt_date(last_ts.timestamp() * 1000)
                        last_ts = int(last_ts.timestamp() * 1000)
                        self.RedisConnection.lpush(output_key, json.dumps([ct, last_ts, dt] + last_data))
                last_ts = ts
                last_data = data
