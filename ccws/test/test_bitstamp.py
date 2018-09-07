from interruptingcow import timeout
from ccws.bitstamp import Bitstamp
from ccws.test.test_base import Test
from ccws.configs import HOME_PATH


class TestBitstamp(Test, Bitstamp):
    def __init__(self, *args, **kwargs):
        Bitstamp.__init__(self)
        Test.__init__(self, *args, **kwargs)

    def test_BTC_USD_order(self):
        origin = {
            'FileName': 'BTC_USD-bitstamp_order.gz',
            'Date': '2018/07/20',
            'Output': 'BTC_USD-bitstamp.book.csv.gz',
        }
        self.initialization('BTC/USD', 'order', origin['Date'])

        input_key = self.Config['RedisCollectKey']
        self.write_into_redis(input_key, self.RedisConnection, origin['FileName'])

        try:
            with timeout(15, exception=RuntimeWarning):
                self.process_data()
        except RuntimeWarning:
            pass

        try:
            with timeout(15, exception=RuntimeWarning):
                self.write_data_csv()
        except RuntimeWarning:
            pass

        fn1 = origin['Output']
        fn2 = '%s/%s/%s' % (HOME_PATH, origin['Date'], self.Config['FileName'])
        self.compare_two_csv(fn1, fn2)
        self.delete_tmp_file(fn2)

    def test_BTC_USD_trade(self):
        origin = {
            'FileName': 'BTC_USD-bitstamp_ticker.gz',
            'Date': '2018/07/20',
            'Output': 'BTC_USD-bitstamp.trade.csv.gz',
        }
        self.initialization('BTC/USD', 'trade', origin['Date'])

        input_key = self.Config['RedisCollectKey']
        self.write_into_redis(input_key, self.RedisConnection, origin['FileName'])

        try:
            with timeout(5, exception=RuntimeWarning):
                self.process_data()
        except RuntimeWarning:
            pass

        try:
            with timeout(5, exception=RuntimeWarning):
                self.write_data_csv()
        except RuntimeWarning:
            pass

        fn1 = origin['Output']
        fn2 = '%s/%s/%s' % (HOME_PATH, origin['Date'], self.Config['FileName'])
        self.compare_two_csv(fn1, fn2)
        self.delete_tmp_file(fn2)

    def test_BCH_USD_order(self):
        origin = {
            'FileName': 'BCH_USD-bitstamp_order.gz',
            'Date': '2018/07/24',
            'Output': 'BCH_USD-bitstamp.book.csv.gz',
        }
        self.initialization('BCH/USD', 'order', origin['Date'])

        input_key = self.Config['RedisCollectKey']
        self.write_into_redis(input_key, self.RedisConnection, origin['FileName'])

        try:
            with timeout(25, exception=RuntimeWarning):
                self.process_data()
        except RuntimeWarning:
            pass

        try:
            with timeout(25, exception=RuntimeWarning):
                self.write_data_csv()
        except RuntimeWarning:
            pass

        fn1 = origin['Output']
        fn2 = '%s/%s/%s' % (HOME_PATH, origin['Date'], self.Config['FileName'])
        self.compare_two_csv(fn1, fn2)
        self.delete_tmp_file(fn2)

    def test_BCH_USD_trade(self):
        origin = {
            'FileName': 'BCH_USD-bitstamp_ticker.gz',
            'Date': '2018/07/24',
            'Output': 'BCH_USD-bitstamp.trade.csv.gz',
        }
        self.initialization('BCH/USD', 'trade', origin['Date'])

        input_key = self.Config['RedisCollectKey']
        self.write_into_redis(input_key, self.RedisConnection, origin['FileName'])

        try:
            with timeout(5, exception=RuntimeWarning):
                self.process_data()
        except RuntimeWarning:
            pass

        try:
            with timeout(5, exception=RuntimeWarning):
                self.write_data_csv()
        except RuntimeWarning:
            pass

        fn1 = origin['Output']
        fn2 = '%s/%s/%s' % (HOME_PATH, origin['Date'], self.Config['FileName'])
        self.compare_two_csv(fn1, fn2)
        self.delete_tmp_file(fn2)

    def test_ETH_USD_order(self):
        origin = {
            'FileName': 'ETH_USD-bitstamp_order.gz',
            'Date': '2018/07/24',
            'Output': 'ETH_USD-bitstamp.book.csv.gz',
        }
        self.initialization('ETH/USD', 'order', origin['Date'])

        input_key = self.Config['RedisCollectKey']
        self.write_into_redis(input_key, self.RedisConnection, origin['FileName'])

        try:
            with timeout(25, exception=RuntimeWarning):
                self.process_data()
        except RuntimeWarning:
            pass

        try:
            with timeout(25, exception=RuntimeWarning):
                self.write_data_csv()
        except RuntimeWarning:
            pass

        fn1 = origin['Output']
        fn2 = '%s/%s/%s' % (HOME_PATH, origin['Date'], self.Config['FileName'])
        self.compare_two_csv(fn1, fn2)
        self.delete_tmp_file(fn2)

    def test_ETH_USD_trade(self):
        origin = {
            'FileName': 'ETH_USD-bitstamp_ticker.gz',
            'Date': '2018/07/24',
            'Output': 'ETH_USD-bitstamp.trade.csv.gz',
        }
        self.initialization('ETH/USD', 'trade', origin['Date'])

        input_key = self.Config['RedisCollectKey']
        self.write_into_redis(input_key, self.RedisConnection, origin['FileName'])

        try:
            with timeout(5, exception=RuntimeWarning):
                self.process_data()
        except RuntimeWarning:
            pass

        try:
            with timeout(5, exception=RuntimeWarning):
                self.write_data_csv()
        except RuntimeWarning:
            pass

        fn1 = origin['Output']
        fn2 = '%s/%s/%s' % (HOME_PATH, origin['Date'], self.Config['FileName'])
        self.compare_two_csv(fn1, fn2)
        self.delete_tmp_file(fn2)

    def test_XRP_USD_order(self):
        origin = {
            'FileName': 'XRP_USD-bitstamp_order.gz',
            'Date': '2018/08/08',
            'Output': 'XRP_USD-bitstamp.book.csv.gz',
        }
        self.initialization('XRP/USD', 'order', origin['Date'])

        input_key = self.Config['RedisCollectKey']
        self.write_into_redis(input_key, self.RedisConnection, origin['FileName'])

        try:
            with timeout(15, exception=RuntimeWarning):
                self.process_data()
        except RuntimeWarning:
            pass

        try:
            with timeout(15, exception=RuntimeWarning):
                self.write_data_csv()
        except RuntimeWarning:
            pass

        fn1 = origin['Output']
        fn2 = '%s/%s/%s' % (HOME_PATH, origin['Date'], self.Config['FileName'])
        self.compare_two_csv(fn1, fn2)
        self.delete_tmp_file(fn2)

    def test_XRP_USD_trade(self):
        origin = {
            'FileName': 'XRP_USD-bitstamp_ticker.gz',
            'Date': '2018/08/08',
            'Output': 'XRP_USD-bitstamp.trade.csv.gz',
        }
        self.initialization('XRP/USD', 'trade', origin['Date'])

        input_key = self.Config['RedisCollectKey']
        self.write_into_redis(input_key, self.RedisConnection, origin['FileName'])

        try:
            with timeout(5, exception=RuntimeWarning):
                self.process_data()
        except RuntimeWarning:
            pass

        try:
            with timeout(5, exception=RuntimeWarning):
                self.write_data_csv()
        except RuntimeWarning:
            pass

        fn1 = origin['Output']
        fn2 = '%s/%s/%s' % (HOME_PATH, origin['Date'], self.Config['FileName'])
        self.compare_two_csv(fn1, fn2)
        self.delete_tmp_file(fn2)

