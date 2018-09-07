# coding=utf-8

import json
import time
from hftcoin.mdagent.ccws import Exchange


class Binance(Exchange):
    ExchangeId = 'Binance'

    def collect_data(self):
        self.connect_redis()
        self.run_websocketapp(
            url_append=self.Config['url_append']
        )

    def process_order_data(self):
        input_key = self.Config['RedisCollectKey']
        output_key = self.Config['RedisOutputKey']
        last_id = -100
        book_pre = []
        while True:
            if self.RedisConnection.llen(input_key) < 1:
                time.sleep(60)
                continue
            [ct, msg] = json.loads(self.RedisConnection.rpop(input_key).decode('utf-8'))
            ts, msg = ct, json.loads(msg)
            uid = int(msg.get('lastUpdateId', 0))
            if last_id != -100 and uid < last_id:
                self.Logger.warning('Missing Data in front of %d' % uid)
            dt = self.fmt_date(ts)
            asks, bids = msg.get('asks'), msg.get('bids')
            asks = [[float(x[i]) for i in range(2)] for x in asks]
            bids = [[float(x[i]) for i in range(2)] for x in bids]
            bids.sort(key=lambda x: x[0], reverse=True)
            asks.sort(key=lambda x: x[0])
            book = bids + asks
            book = sum(book, [])
            last_id = uid
            if book == book_pre:
                continue
            book_pre = book
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
            ts = int(msg.get('T', 0))
            dt = self.fmt_date(ts)
            con = ['q', 'p', 'E', 't', 'b', 'a']
            data = [msg.get(k) for k in con]
            self.RedisConnection.lpush(output_key, json.dumps([ct, ts, dt] + data))

    @staticmethod
    def get(l, p):
        for i in range(len(l)):
            if abs(l[i][0] - p) < 0.01:
                return i
        return -1

    def process_order_book_update_info(self):
        input_key = self.Config['RedisCollectKey']
        bids, asks, books, trades, trade_bid_tmp, trade_ask_tmp = [], [], [], [], [], []
        tag = -1  # 0 for depth and 1 for trade
        start_point = 1000
        buf = 100
        while True:
            if self.RedisConnection.llen(input_key) < 1:
                print(trades[4], trades[5])
                print(len(trades))
                time.sleep(60)
                continue
            [ct, msg] = json.loads(self.RedisConnection.rpop(input_key).decode('utf-8'))
            msg = json.loads(msg)
            if msg['stream'].endswith('trade') and start_point == 0:
                if tag == 0:
                    trade_bid_tmp, trade_ask_tmp = [], []
                data = msg['data']
                price, size = float(data['p']), float(data['q'])
                if data['m']:
                    num = self.get(trade_bid_tmp, price)
                    if num == -1:
                        trade_bid_tmp.append([price, size, 0, data['E']])
                    else:
                        trade_bid_tmp[num][1] += size
                else:
                    num = self.get(trade_ask_tmp, price)
                    if num == -1:
                        trade_ask_tmp.append([price, size, 1, data['E']])
                    else:
                        trade_ask_tmp[num][1] += size
                tag = 1
            elif msg['stream'].endswith('depth'):
                if tag == 1:
                    trades.extend(trade_bid_tmp)
                    trades.extend(trade_ask_tmp)
                if start_point > 0:
                    start_point -= 1
                data = msg['data']
                ts = data['E']
                data['b'] = [[float(i[0]), float(i[1])] for i in data['b']]
                data['a'] = [[float(i[0]), float(i[1])] for i in data['a']]
                for i in data['b']:
                    num = self.get(bids, i[0])
                    if num == -1:
                        # add
                        bids.append([i[0], i[1]])
                    else:
                        # add
                        if i[1] < bids[num][1]:
                            books.append([i[0], bids[num][1] - i[1], 0, ts])
                            buf -= 1
                        if i[1] > 1e-8:
                            bids[num][1] = i[1]
                        else:
                            bids.pop(num)
                for i in data['a']:
                    num = self.get(asks, i[0])
                    if num == -1:
                        # add
                        asks.append([i[0], i[1]])
                    else:
                        # add
                        if i[1] < asks[num][1]:
                            books.append([i[0], asks[num][1] - i[1], 1, ts])
                            buf -= 1
                        if i[1] > 1e-8:
                            asks[num][1] = i[1]
                        else:
                            asks.pop(num)
                tag = 0
            if buf < 0 and start_point == 0:
                buf = 100
                now = books[-1][3]
                i = 0
                while i < len(books):
                    for j in range(len(trades)):
                        # if time_gap changes to 2s, mismatch will reduce 1(19->18)
                        if trades[j][3] - books[i][3] > 1000:
                            break
                        if (abs(books[i][0] - trades[j][0]) < 0.01) and (abs(books[i][1] - trades[j][1]) < 1e-8) and (
                                abs(books[i][3] - trades[j][3]) < 1000) and (books[i][2] == trades[j][2]):
                            trades.pop(j)
                            books.pop(i)
                            i -= 1
                            break
                    if now - books[i][3] > 1000:
                        books.pop(i)
                        i -= 1
                    i += 1







