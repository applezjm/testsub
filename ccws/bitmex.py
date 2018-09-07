# coding=utf-8

import json
import time
from hftcoin.mdagent.ccws import Exchange


class Bitmex(Exchange):
    ExchangeId = 'Bitmex'

    def collect_data(self):
        self.connect_redis()
        self.run_websocketapp(
            on_open=self.on_open,
        )

    def on_open(self, ws):
        ws.send(json.dumps(self.Config['Subscription']))
        self.Logger.info('Subscription')

    def process_order_book_10_data(self):
        input_key = self.Config['RedisCollectKey']
        output_key = self.Config['RedisOutputKey']
        while True:
            if self.RedisConnection.llen(input_key) < 1:
                time.sleep(60)
                continue
            [ct, msg] = json.loads(self.RedisConnection.rpop(input_key).decode('utf-8'))
            msg = json.loads(msg)
            if msg.get('action', None) == 'update':
                data = msg.get('data', None)
                data = data[0]
                ts = self.date_from_str(data.get('timestamp', '2010-01-01T00:00:01.000000Z'))
                dt = self.fmt_date(ts.timestamp() * 1000)
                ts = int(ts.timestamp() * 1000)
                asks = [[float(i) for i in j] for j in data.get('asks')]
                bids = [[float(i) for i in j] for j in data.get('bids')]
                bids.sort(key=lambda x: x[0], reverse=True)
                asks.sort(key=lambda x: x[0])
                book = bids + asks
                book = sum(book, [])
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
                ts = self.date_from_str(event.get('timestamp', '2010-01-01T00:00:01.000000Z'))
                dt = self.fmt_date(ts.timestamp() * 1000)
                ts = int(ts.timestamp() * 1000)
                self.RedisConnection.lpush(output_key, json.dumps([ct, ts, dt] + data))

    @staticmethod
    def get(l, p):
        for i in range(len(l)):
            if l[i][2] == p:
                return i
        return -1

    def process_order_book_update_info(self):
        input_key = self.Config['RedisCollectKey']
        bids, asks, books, trades = [], [], [], []
        is_initialized = False
        buf = 100
        while True:
            if self.RedisConnection.llen(input_key) < 1:
                print(len(trades))
                time.sleep(60)
                continue
            [ct, msg] = json.loads(self.RedisConnection.rpop(input_key).decode('utf-8'))
            msg = json.loads(msg)
            if 'table' not in msg.keys():
                continue
            if msg['table'] == 'orderBookL2':
                if msg['action'] == 'partial':
                    is_initialized = True
                    for data in msg['data']:
                        alias = bids if data['side'] == 'Buy' else asks
                        alias.append([data['price'], data['size'], data['id']])
                elif is_initialized and msg['action'] == 'insert':
                    for data in msg['data']:
                        alias = bids if data['side'] == 'Buy' else asks
                        alias.append([data['price'], data['size'], data['id']])
                elif is_initialized and msg['action'] == 'delete':
                    for data in msg['data']:
                        alias = bids if data['side'] == 'Buy' else asks
                        num = self.get(alias, data['id'])
                        books.append([alias[num][0], alias[num][1], data['side'], ct])
                        alias.pop(num)
                        buf -= 1
                elif is_initialized and msg['action'] == 'update':
                    for data in msg['data']:
                        alias = bids if data['side'] == 'Buy' else asks
                        num = self.get(alias, data['id'])
                        if alias[num][1] > data['size']:
                            books.append([alias[num][0], alias[num][1] - data['size'], data['side'], ct])
                            buf -= 1
                        alias[num][1] = data['size']
            elif msg['table'] == 'trade':
                trade_tmp = []
                for data in msg['data']:
                    # no timestamp in order, use ts or ct???
                    ts = int(self.date_from_str(data['timestamp']).timestamp() * 1000)
                    data['side'] = 'Buy' if data['side'] == 'Sell' else 'Sell'
                    if trade_tmp:
                        if abs(data['price'] - trade_tmp[0]) < 0.01 and data['side'] == trade_tmp[2]:
                            trade_tmp[1] += data['size']
                        else:
                            trades.append(trade_tmp)
                            trade_tmp = [data['price'], data['size'], data['side'], ct]
                    else:
                        trade_tmp = [data['price'], data['size'], data['side'], ct]
                trades.append(trade_tmp)
            if buf < 0:
                buf = 100
                now = books[-1][3]
                i = 0
                while i < len(books):
                    for j in range(len(trades)):
                        # if time_gap changes to 2s, mismatch will reduce 1(19->18)
                        if trades[j][3] - books[i][3] > 1000:
                            break
                        if (abs(books[i][0] - trades[j][0]) < 0.01) and (abs(books[i][1] - trades[j][1]) < 1e-8) and (abs(books[i][3] - trades[j][3]) < 1000) and (books[i][2] == trades[j][2]):
                            trades.pop(j)
                            books.pop(i)
                            i -= 1
                            break
                    if now - books[i][3] > 1000:
                        books.pop(i)
                        i -= 1
                    i += 1





