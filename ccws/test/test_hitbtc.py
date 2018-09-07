from interruptingcow import timeout
from ccws.hitbtc import Hitbtc
from ccws.test.test_base import Test
from ccws.configs import HOME_PATH


class TestHitbtc(Test, Hitbtc):
    def __init__(self, *args, **kwargs):
        Hitbtc.__init__(self)
        Test.__init__(self, *args, **kwargs)

    def test_BTC_USD_order(self):
        origin = {
            'FileName': 'BTC_USD-hitbtc_order.gz',
            'Date': '2018/07/18',
            'Output': 'BTC_USD-hitbtc.book.csv.gz',
        }
        self.initialization('BTC/USD', 'order', origin['Date'])

        input_key = self.Config['RedisCollectKey']
        self.write_into_redis(input_key, self.RedisConnection, origin['FileName'])

        try:
            with timeout(20, exception=RuntimeWarning):
                self.process_data()
        except RuntimeWarning:
            pass

        try:
            with timeout(20, exception=RuntimeWarning):
                self.write_data_csv()
        except RuntimeWarning:
            pass

        fn1 = origin['Output']
        fn2 = '%s/%s/%s' % (HOME_PATH, origin['Date'], self.Config['FileName'])
        self.compare_two_csv(fn1, fn2)
        self.delete_tmp_file(fn2)

    def test_BTC_USD_trade(self):
        origin = {
            'FileName': 'BTC_USD-hitbtc_ticker.gz',
            'Date': '2018/07/18',
            'Output': 'BTC_USD-hitbtc.trade.csv.gz',
        }
        self.initialization('BTC/USD', 'trade', origin['Date'])

        input_key = self.Config['RedisCollectKey']
        self.write_into_redis(input_key, self.RedisConnection, origin['FileName'])

        try:
            with timeout(10, exception=RuntimeWarning):
                self.process_data()
        except RuntimeWarning:
            pass

        try:
            with timeout(10, exception=RuntimeWarning):
                self.write_data_csv()
        except RuntimeWarning:
            pass

        fn1 = origin['Output']
        fn2 = '%s/%s/%s' % (HOME_PATH, origin['Date'], self.Config['FileName'])
        self.compare_two_csv(fn1, fn2)
        self.delete_tmp_file(fn2)

    def test_BCH_USD_order(self):
        origin = {
            'FileName': 'BCH_USD-hitbtc_order.gz',
            'Date': '2018/07/18',
            'Output': 'BCH_USD-hitbtc.book.csv.gz',
        }
        self.initialization('BCH/USD', 'order', origin['Date'])

        input_key = self.Config['RedisCollectKey']
        self.write_into_redis(input_key, self.RedisConnection, origin['FileName'])

        try:
            with timeout(20, exception=RuntimeWarning):
                self.process_data()
        except RuntimeWarning:
            pass

        try:
            with timeout(20, exception=RuntimeWarning):
                self.write_data_csv()
        except RuntimeWarning:
            pass

        fn1 = origin['Output']
        fn2 = '%s/%s/%s' % (HOME_PATH, origin['Date'], self.Config['FileName'])
        self.compare_two_csv(fn1, fn2)
        self.delete_tmp_file(fn2)

    def test_BCH_USD_trade(self):
        origin = {
            'FileName': 'BCH_USD-hitbtc_ticker.gz',
            'Date': '2018/07/19',
            'Output': 'BCH_USD-hitbtc.trade.csv.gz',
        }
        self.initialization('BCH/USD', 'trade', origin['Date'])

        input_key = self.Config['RedisCollectKey']
        self.write_into_redis(input_key, self.RedisConnection, origin['FileName'])

        try:
            with timeout(10, exception=RuntimeWarning):
                self.process_data()
        except RuntimeWarning:
            pass

        try:
            with timeout(10, exception=RuntimeWarning):
                self.write_data_csv()
        except RuntimeWarning:
            pass

        fn1 = origin['Output']
        fn2 = '%s/%s/%s' % (HOME_PATH, origin['Date'], self.Config['FileName'])
        self.compare_two_csv(fn1, fn2)
        self.delete_tmp_file(fn2)

    def test_ETH_USD_order(self):
        origin = {
            'FileName': 'ETH_USD-hitbtc_order.gz',
            'Date': '2018/07/18',
            'Output': 'ETH_USD-hitbtc.book.csv.gz',
        }
        self.initialization('ETH/USD', 'order', origin['Date'])

        input_key = self.Config['RedisCollectKey']
        self.write_into_redis(input_key, self.RedisConnection, origin['FileName'])

        try:
            with timeout(20, exception=RuntimeWarning):
                self.process_data()
        except RuntimeWarning:
            pass

        try:
            with timeout(20, exception=RuntimeWarning):
                self.write_data_csv()
        except RuntimeWarning:
            pass

        fn1 = origin['Output']
        fn2 = '%s/%s/%s' % (HOME_PATH, origin['Date'], self.Config['FileName'])
        self.compare_two_csv(fn1, fn2)
        self.delete_tmp_file(fn2)

    def test_ETH_USD_trade(self):
        origin = {
            'FileName': 'ETH_USD-hitbtc_ticker.gz',
            'Date': '2018/07/19',
            'Output': 'ETH_USD-hitbtc.trade.csv.gz',
        }
        self.initialization('ETH/USD', 'trade', origin['Date'])

        input_key = self.Config['RedisCollectKey']
        self.write_into_redis(input_key, self.RedisConnection, origin['FileName'])

        try:
            with timeout(10, exception=RuntimeWarning):
                self.process_data()
        except RuntimeWarning:
            pass

        try:
            with timeout(10, exception=RuntimeWarning):
                self.write_data_csv()
        except RuntimeWarning:
            pass

        fn1 = origin['Output']
        fn2 = '%s/%s/%s' % (HOME_PATH, origin['Date'], self.Config['FileName'])
        self.compare_two_csv(fn1, fn2)
        self.delete_tmp_file(fn2)

    def test_XRP_USD_order(self):
        origin = {
            'FileName': 'XRP_USD-hitbtc_order.gz',
            'Date': '2018/08/09',
            'Output': 'XRP_USD-hitbtc.book.csv.gz',
        }
        self.initialization('XRP/USD', 'order', origin['Date'])

        input_key = self.Config['RedisCollectKey']
        self.write_into_redis(input_key, self.RedisConnection, origin['FileName'])

        try:
            with timeout(10, exception=RuntimeWarning):
                self.process_data()
        except RuntimeWarning:
            pass

        try:
            with timeout(10, exception=RuntimeWarning):
                self.write_data_csv()
        except RuntimeWarning:
            pass

        fn1 = origin['Output']
        fn2 = '%s/%s/%s' % (HOME_PATH, origin['Date'], self.Config['FileName'])
        self.compare_two_csv(fn1, fn2)
        self.delete_tmp_file(fn2)

    def test_XRP_USD_trade(self):
        origin = {
            'FileName': 'XRP_USD-hitbtc_ticker.gz',
            'Date': '2018/08/09',
            'Output': 'XRP_USD-hitbtc.trade.csv.gz',
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

    def test_EOS_USD_order(self):
        origin = {
            'FileName': 'EOS_USD-hitbtc_order.gz',
            'Date': '2018/08/09',
            'Output': 'EOS_USD-hitbtc.book.csv.gz',
        }
        self.initialization('EOS/USD', 'order', origin['Date'])

        input_key = self.Config['RedisCollectKey']
        self.write_into_redis(input_key, self.RedisConnection, origin['FileName'])

        try:
            with timeout(10, exception=RuntimeWarning):
                self.process_data()
        except RuntimeWarning:
            pass

        try:
            with timeout(10, exception=RuntimeWarning):
                self.write_data_csv()
        except RuntimeWarning:
            pass

        fn1 = origin['Output']
        fn2 = '%s/%s/%s' % (HOME_PATH, origin['Date'], self.Config['FileName'])
        self.compare_two_csv(fn1, fn2)
        self.delete_tmp_file(fn2)

    def test_EOS_USD_trade(self):
        origin = {
            'FileName': 'EOS_USD-hitbtc_ticker.gz',
            'Date': '2018/08/09',
            'Output': 'EOS_USD-hitbtc.trade.csv.gz',
        }
        self.initialization('EOS/USD', 'trade', origin['Date'])

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


