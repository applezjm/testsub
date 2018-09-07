from interruptingcow import timeout
from ccws.huobipro import Huobipro
from ccws.test.test_base import Test
from ccws.configs import HOME_PATH


class TestHuobipro(Test, Huobipro):
    def __init__(self, *args, **kwargs):
        Huobipro.__init__(self)
        Test.__init__(self, *args, **kwargs)

    def test_BTC_USDT_order(self):
        origin = {
            'FileName': 'BTC_USDT-huobipro_order.gz',
            'Date': '2018/08/08',
            'Output': 'BTC_USDT-huobipro.book.csv.gz',
        }
        self.initialization('BTC/USDT', 'order', origin['Date'])

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

    def test_BTC_USDT_ticker(self):
        origin = {
            'FileName': 'BTC_USDT-huobipro_ticker.gz',
            'Date': '2018/08/08',
            'Output': 'BTC_USDT-huobipro.trade.csv.gz',
        }
        self.initialization('BTC/USDT', 'trade', origin['Date'])

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

    def test_BCH_USDT_order(self):
        origin = {
            'FileName': 'BCH_USDT-huobipro_order.gz',
            'Date': '2018/08/08',
            'Output': 'BCH_USDT-huobipro.book.csv.gz',
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
            'FileName': 'BCH_USDT-huobipro_ticker.gz',
            'Date': '2018/08/08',
            'Output': 'BCH_USDT-huobipro.trade.csv.gz',
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
            'FileName': 'ETH_USDT-huobipro_order.gz',
            'Date': '2018/08/08',
            'Output': 'ETH_USDT-huobipro.book.csv.gz',
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
            'FileName': 'ETH_USDT-huobipro_ticker.gz',
            'Date': '2018/08/08',
            'Output': 'ETH_USDT-huobipro.trade.csv.gz',
        }
        self.initialization('ETH/USDT', 'trade', origin['Date'])

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

    def test_EOS_USDT_order(self):
        origin = {
            'FileName': 'EOS_USDT-huobipro_order.gz',
            'Date': '2018/08/08',
            'Output': 'EOS_USDT-huobipro.book.csv.gz',
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
            'FileName': 'EOS_USDT-huobipro_ticker.gz',
            'Date': '2018/08/08',
            'Output': 'EOS_USDT-huobipro.trade.csv.gz',
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
            'FileName': 'XRP_USDT-huobipro_order.gz',
            'Date': '2018/08/08',
            'Output': 'XRP_USDT-huobipro.book.csv.gz',
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
            'FileName': 'XRP_USDT-huobipro_ticker.gz',
            'Date': '2018/08/08',
            'Output': 'XRP_USDT-huobipro.trade.csv.gz',
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
