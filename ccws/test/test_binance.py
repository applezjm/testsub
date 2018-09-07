from interruptingcow import timeout
from ccws.binance import Binance
from ccws.test.test_base import Test
from ccws.configs import HOME_PATH


class TestBinance(Test, Binance):
    def __init__(self, *args, **kwargs):
        Binance.__init__(self)
        Test.__init__(self, *args, **kwargs)

    def test_BTC_USDT_order(self):
        origin = {
            'FileName': 'BTC_USDT-binance_order.gz',
            'Date': '2018/06/06',
            'Output': 'BTC_USDT-binance.book.csv.gz',
        }
        self.initialization('BTC/USDT', 'order', origin['Date'])

        input_key = self.Config['RedisCollectKey']
        self.write_into_redis(input_key, self.RedisConnection, origin['FileName'])

        try:
            with timeout(5, exception=RuntimeWarning):
                self.process_data()
        except RuntimeWarning:
            pass

        try:
            with timeout(8, exception=RuntimeWarning):
                self.write_data_csv()
        except RuntimeWarning:
            pass

        fn1 = origin['Output']
        fn2 = '%s/%s/%s' % (HOME_PATH, origin['Date'], self.Config['FileName'])
        self.compare_two_csv(fn1, fn2)
        self.delete_tmp_file(fn2)

    def test_BTC_USDT_update(self):
        origin = {
            'FileName': 'full.gz',
            'Date': '2018/08/24',
        }
        self.initialization('BTC/USDT', 'update', origin['Date'])

        input_key = self.Config['RedisCollectKey']
        self.write_into_redis(input_key, self.RedisConnection, origin['FileName'])

        try:
            with timeout(100, exception=RuntimeWarning):
                self.process_data()
        except RuntimeWarning:
            pass

    def test_BTC_USDT_ticker(self):
        origin = {
            'FileName': 'BTC_USDT-binance_ticker.gz',
            'Date': '2018/06/06',
            'Output': 'BTC_USDT-binance.ticker.csv.gz',
        }
        self.initialization('BTC/USDT', 'trade', origin['Date'])

        input_key = self.Config['RedisCollectKey']
        self.write_into_redis(input_key, self.RedisConnection, origin['FileName'])

        try:
            with timeout(10, exception=RuntimeWarning):
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

    def test_BCH_USDT_order(self):
        origin = {
            'FileName': 'BCH_USDT-binance_order.gz',
            'Date': '2018/08/08',
            'Output': 'BCH_USDT-binance.book.csv.gz',
        }
        self.initialization('BCH/USDT', 'order', origin['Date'])

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

    def test_BCH_USDT_ticker(self):
        origin = {
            'FileName': 'BCH_USDT-binance_ticker.gz',
            'Date': '2018/08/09',
            'Output': 'BCH_USDT-binance.ticker.csv.gz',
        }
        self.initialization('BCH/USDT', 'trade', origin['Date'])

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

    def test_ETH_USDT_order(self):
        origin = {
            'FileName': 'ETH_USDT-binance_order.gz',
            'Date': '2018/08/08',
            'Output': 'ETH_USDT-binance.book.csv.gz',
        }
        self.initialization('ETH/USDT', 'order', origin['Date'])

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

    def test_ETH_USDT_ticker(self):
        origin = {
            'FileName': 'ETH_USDT-binance_ticker.gz',
            'Date': '2018/08/08',
            'Output': 'ETH_USDT-binance.ticker.csv.gz',
        }
        self.initialization('ETH/USDT', 'trade', origin['Date'])

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

    def test_EOS_USDT_order(self):
        origin = {
            'FileName': 'EOS_USDT-binance_order.gz',
            'Date': '2018/08/08',
            'Output': 'EOS_USDT-binance.book.csv.gz',
        }
        self.initialization('EOS/USDT', 'order', origin['Date'])

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

    def test_EOS_USDT_ticker(self):
        origin = {
            'FileName': 'EOS_USDT-binance_ticker.gz',
            'Date': '2018/08/08',
            'Output': 'EOS_USDT-binance.ticker.csv.gz',
        }
        self.initialization('EOS/USDT', 'trade', origin['Date'])

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

    def test_XRP_USDT_order(self):
        origin = {
            'FileName': 'XRP_USDT-binance_order.gz',
            'Date': '2018/08/08',
            'Output': 'XRP_USDT-binance.book.csv.gz',
        }
        self.initialization('XRP/USDT', 'order', origin['Date'])

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

    def test_XRP_USDT_ticker(self):
        origin = {
            'FileName': 'XRP_USDT-binance_ticker.gz',
            'Date': '2018/08/08',
            'Output': 'XRP_USDT-binance.ticker.csv.gz',
        }
        self.initialization('XRP/USDT', 'trade', origin['Date'])

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
