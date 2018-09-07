# coding=utf-8


def order_book_header_with_depth(depth):
    return sum([['bidp%d' % i, 'bidv%d' % i] for i in range(depth)], []) \
           + sum([['askp%d' % i, 'askv%d' % i] for i in range(depth)], [])


HuobiConfigs = {
    'BTC/USDT': {
        'trade': {
            'Subscription': {
                'sub': 'market.btcusdt.trade.detail',
                'id': 'hubiprotrade',
            },
            'Header': [
                'price',
                'amount',
                'direction',
                'id',
            ],
            'FileName': 'BTC_USDT-huobipro.trade.csv',
            'RedisCollectKey': 'huobipro-BTC_USDT-trade_raw',
            'RedisOutputKey': 'huobipro-BTC_USDT-trade_processed',
            'DataHandler': 'process_trade_data',
        },

        'order': {
            'iid': 1003,
            'Subscription': {
                'sub': 'market.btcusdt.depth.step0',
                'id': 'hubiproorderbook',
            },
            'OrderBookDepth': 12,
            'Header': order_book_header_with_depth(12),
            'FileName': 'BTC_USDT-huobipro.book.csv',
            'RedisCollectKey': 'huobipro-BTC_USDT-order_raw',
            'RedisOutputKey': 'huobipro-BTC_USDT-order_processed',
            'DataHandler': 'process_order_book_data',
        },
    },

    'BCH/USDT': {
        'trade': {
            'Subscription': {
                'sub': 'market.bchusdt.trade.detail',
                'id': 'hubiprotrade',
            },
            'Header': [
                'price',
                'amount',
                'direction',
                'id',
            ],
            'FileName': 'BCH_USDT-huobipro.trade.csv',
            'RedisCollectKey': 'huobipro-BCH_USDT-trade_raw',
            'RedisOutputKey': 'huobipro-BCH_USDT-trade_processed',
            'DataHandler': 'process_trade_data',
        },

        'order': {
            'Subscription': {
                'sub': 'market.bchusdt.depth.step0',
                'id': 'hubiproorderbook',
            },
            'OrderBookDepth': 12,
            'Header': order_book_header_with_depth(12),
            'FileName': 'BCH_USDT-huobipro.book.csv',
            'RedisCollectKey': 'huobipro-BCH_USDT-order_raw',
            'RedisOutputKey': 'huobipro-BCH_USDT-order_processed',
            'DataHandler': 'process_order_book_data',
        },
    },

    'ETH/USDT': {
        'trade': {
            'Subscription': {
                'sub': 'market.ethusdt.trade.detail',
                'id': 'hubiprotrade',
            },
            'Header': [
                'price',
                'amount',
                'direction',
                'id',
            ],
            'FileName': 'ETH_USDT-huobipro.trade.csv',
            'RedisCollectKey': 'huobipro-ETH_USDT-trade_raw',
            'RedisOutputKey': 'huobipro-ETH_USDT-trade_processed',
            'DataHandler': 'process_trade_data',
        },

        'order': {
            'Subscription': {
                'sub': 'market.ethusdt.depth.step0',
                'id': 'hubiproorderbook',
            },
            'OrderBookDepth': 12,
            'Header': order_book_header_with_depth(12),
            'FileName': 'ETH_USDT-huobipro.book.csv',
            'RedisCollectKey': 'huobipro-ETH_USDT-order_raw',
            'RedisOutputKey': 'huobipro-ETH_USDT-order_processed',
            'DataHandler': 'process_order_book_data',
        },
    },

    'EOS/USDT': {
        'trade': {
            'Subscription': {
                'sub': 'market.eosusdt.trade.detail',
                'id': 'hubiprotrade',
            },
            'Header': [
                'price',
                'amount',
                'direction',
                'id',
            ],
            'FileName': 'EOS_USDT-huobipro.trade.csv',
            'RedisCollectKey': 'huobipro-EOS_USDT-trade_raw',
            'RedisOutputKey': 'huobipro-EOS_USDT-trade_processed',
            'DataHandler': 'process_trade_data',
        },

        'order': {
            'Subscription': {
                'sub': 'market.eosusdt.depth.step0',
                'id': 'hubiproorderbook',
            },
            'OrderBookDepth': 12,
            'Header': order_book_header_with_depth(12),
            'FileName': 'EOS_USDT-huobipro.book.csv',
            'RedisCollectKey': 'huobipro-EOS_USDT-order_raw',
            'RedisOutputKey': 'huobipro-EOS_USDT-order_processed',
            'DataHandler': 'process_order_book_data',
        },
    },

    'XRP/USDT': {
        'trade': {
            'Subscription': {
                'sub': 'market.xrpusdt.trade.detail',
                'id': 'hubiprotrade',
            },
            'Header': [
                'price',
                'amount',
                'direction',
                'id',
            ],
            'FileName': 'XRP_USDT-huobipro.trade.csv',
            'RedisCollectKey': 'huobipro-XRP_USDT-trade_raw',
            'RedisOutputKey': 'huobipro-XRP_USDT-trade_processed',
            'DataHandler': 'process_trade_data',
        },

        'order': {
            'Subscription': {
                'sub': 'market.xrpusdt.depth.step0',
                'id': 'hubiproorderbook',
            },
            'OrderBookDepth': 12,
            'Header': order_book_header_with_depth(12),
            'FileName': 'XRP_USDT-huobipro.book.csv',
            'RedisCollectKey': 'huobipro-XRP_USDT-order_raw',
            'RedisOutputKey': 'huobipro-XRP_USDT-order_processed',
            'DataHandler': 'process_order_book_data',
        },
    },
}

GdaxConfigs = {
    'BTC/USD': {
        'trade': {
            'Subscription': {
                'type': 'subscribe',
                'channels': [{'name': 'ticker', 'product_ids': ['BTC-USD']}],
            },
            'Header': [
                'price',
                'last_size',
                'side',
                'best_ask',
                'best_bid',
                'high_24h',
                'low_24h',
                'open_24h',
                'volume_24h',
                'volume_30d',
                'sequence',
                'trade_id',
            ],
            'FileName': 'BTC_USD-gdax.ticker.csv',
            'RedisCollectKey': 'gdax-BTC_USD-ticker_raw',
            'RedisOutputKey': 'gdax-BTC_USD-ticker',
            'DataHandler': 'process_ticker_data',
        },

        'order': {
            'iid': 1001,
            'Subscription': {
                'type': 'subscribe',
                'channels': [{'name': 'level2', 'product_ids': ['BTC-USD']}],
            },
            'OrderBookDepth': 12,
            'Header': ['IsSnapShot'] + order_book_header_with_depth(12),
            'FileName': 'BTC_USD-gdax.book.csv',
            'RedisCollectKey': 'gdax-BTC_USD-order_raw',
            'RedisOutputKey': 'gdax-BTC_USD-order_processed',
            'DataHandler': 'process_order_book_data',
            'TickSize': 0.01,
            'AmountMin': 1e-8,
        },

        'update': {
            'Subscription': {
                'type': 'subscribe',
                'channels': [{'name': 'full', 'product_ids': ['BTC-USD']}],
            },
            'Header': [
                'price',
                'size',
                'side',
                'type',
            ],
            'FileName': 'BTC_USD-gdax.trade.csv',
            'RedisCollectKey': 'gdax-BTC_USD-order-update_raw',
            'RedisOutputKey': 'gdax-BTC_USD-order-update_processed',
            'DataHandler': 'process_order_book_update_info',
        },
    },

    'BCH/USD': {

        'trade': {
            'Subscription': {
                'type': 'subscribe',
                'channels': [{'name': 'ticker', 'product_ids': ['BCH-USD']}],
            },
            'Header': [
                'price',
                'last_size',
                'side',
                'best_ask',
                'best_bid',
                'high_24h',
                'low_24h',
                'open_24h',
                'volume_24h',
                'volume_30d',
                'sequence',
                'trade_id',
            ],
            'FileName': 'BCH_USD-gdax.ticker.csv',
            'RedisCollectKey': 'gdax-BCH_USD-ticker_raw',
            'RedisOutputKey': 'gdax-BCH_USD-ticker',
            'DataHandler': 'process_ticker_data',
        },

        'order': {
            'Subscription': {
                'type': 'subscribe',
                'channels': [{'name': 'level2', 'product_ids': ['BCH-USD']}],
            },
            'OrderBookDepth': 5,
            'Header': ['IsSnapShot'] + order_book_header_with_depth(5),
            'FileName': 'BCH_USD-gdax.book.csv',
            'RedisCollectKey': 'gdax-BCH_USD-order_raw',
            'RedisOutputKey': 'gdax-BCH_USD-order_processed',
            'DataHandler': 'process_order_book_data',
            'TickSize': 0.01,
            'AmountMin': 1e-8,
        },

    },

    'ETH/USD': {

        'trade': {
            'Subscription': {
                'type': 'subscribe',
                'channels': [{'name': 'ticker', 'product_ids': ['ETH-USD']}],
            },
            'Header': [
                'price',
                'last_size',
                'side',
                'best_ask',
                'best_bid',
                'high_24h',
                'low_24h',
                'open_24h',
                'volume_24h',
                'volume_30d',
                'sequence',
                'trade_id',
            ],
            'FileName': 'ETH_USD-gdax.ticker.csv',
            'RedisCollectKey': 'gdax-ETH_USD-ticker_raw',
            'RedisOutputKey': 'gdax-ETH_USD-ticker',
            'DataHandler': 'process_ticker_data',
        },

        'order': {
            'Subscription': {
                'type': 'subscribe',
                'channels': [{'name': 'level2', 'product_ids': ['ETH-USD']}],
            },
            'OrderBookDepth': 12,
            'Header': ['IsSnapShot'] + order_book_header_with_depth(12),
            'FileName': 'ETH_USD-gdax.book.csv',
            'RedisCollectKey': 'gdax-ETH_USD-order_raw',
            'RedisOutputKey': 'gdax-ETH_USD-order_processed',
            'DataHandler': 'process_order_book_data',
            'TickSize': 0.01,
            'AmountMin': 1e-8,
        },

    },

}

_gemini_trade_info_header = [
    'tid',
    'makerSide',
    'price',
    'amount',
]

# noinspection PyPep8
GeminiConfigs = {
    'BTC/USD': {
        'order': {
            'url_append': '/marketdata/BTCUSD',
            'OrderBookDepth': 12,
            'Header': ['IsSnapShot'] + order_book_header_with_depth(12) + _gemini_trade_info_header + ['lasttradetime'],
            'TradeInfoHeader': _gemini_trade_info_header,
            'FileName': 'BTC_USD-gemini.book.csv',
            'RedisCollectKey': 'gemini-BTC_USD_raw',
            'RedisOutputKey': 'gemini-BTC_USD_processed',
            'DataHandler': 'process_order_data',
            'TickSize': 0.01,
            'AmountMin': 1e-8,
        },

        'update': {
            'url_append': '/marketdata/BTCUSD',
            'Header': [
                'price',
                'size',
                'side',
                'type',
            ],
            'FileName': 'BTC_USD-gemini.trade.csv',
            'RedisCollectKey': 'gemini-BTC_USD-order-update_raw',
            'RedisOutputKey': 'gemini-BTC_USD-update_processed',
            'DataHandler': 'process_order_book_update_info',
        },
    },

    'ETH/USD': {
        'order': {
            'url_append': '/marketdata/ETHUSD',
            'OrderBookDepth': 12,
            'Header': ['IsSnapShot'] + order_book_header_with_depth(12) + _gemini_trade_info_header + ['lasttradetime'],
            'TradeInfoHeader': _gemini_trade_info_header,
            'FileName': 'ETH_USD-gemini.book.csv',
            'RedisCollectKey': 'gemini-ETH_USD_raw',
            'RedisOutputKey': 'gemini-ETH_USD_processed',
            'DataHandler': 'process_order_data',
            'TickSize': 0.01,
            'AmountMin': 1e-8,
        },
    },
}

BitmexConfigs = {
    'BTC/USD': {
        'trade': {
            'Subscription': {
                'op': 'subscribe',
                'args': ["trade:XBTUSD"],
            },
            'Header': [
                'side',
                'size',
                'price',
                'tickDirection',
                'trdMatchID',
                'grossValue',
                'homeNotional',
                'foreignNotional',
            ],
            'FileName': 'BTC_USD-bitmex.trade.csv',
            'RedisCollectKey': 'bitmex-BTC_USD-trade_raw',
            'RedisOutputKey': 'bitmex-BTC_USD-trade_processed',
            'DataHandler': 'process_trade_data',
        },

        'order': {
            'iid': 1002,
            'Subscription': {
                'op': 'subscribe',
                'args': ["orderBook10:XBTUSD"],
            },
            'OrderBookDepth': 10,
            'Header': order_book_header_with_depth(10),
            'FileName': 'BTC_USD-bitmex.book.csv',
            'RedisCollectKey': 'bitmex-BTC_USD-orderBook10_raw',
            'RedisOutputKey': 'bitmex-BTC_USD-orderBook10_processed',
            'DataHandler': 'process_order_book_10_data',
            'TickSize': 0.01,
            'AmountMin': 1e-8,
        },

        'update': {
            'Subscription': {
                'op': 'subscribe',
                'args': ["orderBook10:XBTUSD", "trade:XBTUSD"],
            },
            'Header': [
                'side',
                'size',
                'price',
                'tickDirection',
                'trdMatchID',
                'grossValue',
                'homeNotional',
                'foreignNotional',
            ],
            'FileName': 'BTC_USD-bitmex-update.book.csv',
            'RedisCollectKey': 'bitmex-BTC_USD-update_raw',
            'RedisOutputKey': 'bitmex-BTC_USD-update_processed',
            'DataHandler': 'process_order_book_update_info',
        },
    },

    'ETH/USD': {
        'trade': {
            'Subscription': {
                'op': 'subscribe',
                'args': ["trade:ETHUSD"],
            },
            'Header': [
                'side',
                'size',
                'price',
                'tickDirection',
                'trdMatchID',
                'grossValue',
                'homeNotional',
                'foreignNotional',
            ],
            'FileName': 'ETH_USD-bitmex.trade.csv',
            'RedisCollectKey': 'bitmex-ETH_USD-trade_raw',
            'RedisOutputKey': 'bitmex-ETH_USD-trade_processed',
            'DataHandler': 'process_trade_data',
        },

        'order': {
            'Subscription': {
                'op': 'subscribe',
                'args': ["orderBook10:ETHUSD"],
            },
            'OrderBookDepth': 10,
            'Header': order_book_header_with_depth(10),
            'FileName': 'ETH_USD-bitmex.book.csv',
            'RedisCollectKey': 'bitmex-ETH_USD-orderBook10_raw',
            'RedisOutputKey': 'bitmex-ETH_USD-orderBook10_processed',
            'DataHandler': 'process_order_book_10_data',
            'TickSize': 0.01,
            'AmountMin': 1e-8,
        },
    },
}

BinanceConfigs = {
    'BTC/USDT': {
        'order': {
            'iid': 1004,
            'url_append': '/ws/btcusdt@depth20',
            'OrderBookDepth': 20,
            'Header': order_book_header_with_depth(20),
            'FileName': 'BTC_USDT-binance.book.csv',
            'RedisCollectKey': 'binance-BTC_USDT-order_raw',
            'RedisOutputKey': 'binance-BTC_USDT-order_processed',
            'DataHandler': 'process_order_data',
            'TickSize': 0.01,
            'AmountMin': 1e-8,
        },
        'trade': {
            'url_append': '/ws/btcusdt@trade',
            'Header': [
                'size',
                'price',
                'eventtime',
                'tradeId',
                'buyerId',
                'sellerId',
            ],
            'FileName': 'BTC_USDT-binance.ticker.csv',
            'RedisCollectKey': 'binance-BTC_USDT-ticker_raw',
            'RedisOutputKey': 'binance-BTC_USDT-ticker_processed',
            'DataHandler': 'process_trade_data',
        },
        'update': {
            'url_append': '/stream?streams=ws/btcusdt@trade/ws/btcusdt@depth20',
            'Header': [],
            'FileName': 'BTC_USDT-binance.ticker.csv',
            'RedisCollectKey': 'binance-BTC_USDT-update_raw',
            'RedisOutputKey': 'binance-BTC_USDT-update_processed',
            'DataHandler': 'process_order_book_update_info',
        },
    },

    'ETH/USDT': {
        'order': {
            'url_append': '/ws/ethusdt@depth20',
            'OrderBookDepth': 20,
            'Header': order_book_header_with_depth(20),
            'FileName': 'ETH_USDT-binance.book.csv',
            'RedisCollectKey': 'binance-ETH_USDT-order_raw',
            'RedisOutputKey': 'binance-ETH_USDT-order_processed',
            'DataHandler': 'process_order_data',
            'TickSize': 0.01,
            'AmountMin': 1e-8,
        },
        'trade': {
            'url_append': '/ws/ethusdt@trade',
            'Header': [
                'size',
                'price',
                'eventtime',
                'tradeId',
                'buyerId',
                'sellerId',
            ],
            'FileName': 'ETH_USDT-binance.ticker.csv',
            'RedisCollectKey': 'binance-ETH_USDT-ticker_raw',
            'RedisOutputKey': 'binance-ETH_USDT-ticker_processed',
            'DataHandler': 'process_trade_data',
        },
    },

    'BCH/USDT': {
        'order': {
            'url_append': '/ws/bccusdt@depth20',
            'OrderBookDepth': 20,
            'Header': order_book_header_with_depth(20),
            'FileName': 'BCH_USDT-binance.book.csv',
            'RedisCollectKey': 'binance-BCH_USDT-order_raw',
            'RedisOutputKey': 'binance-BCH_USDT-order_processed',
            'DataHandler': 'process_order_data',
            'TickSize': 0.01,
            'AmountMin': 1e-8,
        },
        'trade': {
            'url_append': '/ws/bccusdt@trade',
            'Header': [
                'size',
                'price',
                'eventtime',
                'tradeId',
                'buyerId',
                'sellerId',
            ],
            'FileName': 'BCH_USDT-binance.ticker.csv',
            'RedisCollectKey': 'binance-BCH_USDT-ticker_raw',
            'RedisOutputKey': 'binance-BCH_USDT-ticker_processed',
            'DataHandler': 'process_trade_data',
        },
    },

    'EOS/USDT': {
        'order': {
            'url_append': '/ws/eosusdt@depth20',
            'OrderBookDepth': 20,
            'Header': order_book_header_with_depth(20),
            'FileName': 'EOS_USDT-binance.book.csv',
            'RedisCollectKey': 'binance-EOS_USDT-order_raw',
            'RedisOutputKey': 'binance-EOS_USDT-order_processed',
            'DataHandler': 'process_order_data',
            'TickSize': 0.01,
            'AmountMin': 1e-8,
        },
        'trade': {
            'url_append': '/ws/eosusdt@trade',
            'Header': [
                'size',
                'price',
                'eventtime',
                'tradeId',
                'buyerId',
                'sellerId',
            ],
            'FileName': 'EOS_USDT-binance.ticker.csv',
            'RedisCollectKey': 'binance-EOS_USDT-ticker_raw',
            'RedisOutputKey': 'binance-EOS_USDT-ticker_processed',
            'DataHandler': 'process_trade_data',
        },
    },

    'XRP/USDT': {
        'order': {
            'url_append': '/ws/xrpusdt@depth20',
            'OrderBookDepth': 20,
            'Header': order_book_header_with_depth(20),
            'FileName': 'XRP_USDT-binance.book.csv',
            'RedisCollectKey': 'binance-XRP_USDT-order_raw',
            'RedisOutputKey': 'binance-XRP_USDT-order_processed',
            'DataHandler': 'process_order_data',
            'TickSize': 0.01,
            'AmountMin': 1e-8,
        },
        'trade': {
            'url_append': '/ws/xrpusdt@trade',
            'Header': [
                'size',
                'price',
                'eventtime',
                'tradeId',
                'buyerId',
                'sellerId',
            ],
            'FileName': 'XRP_USDT-binance.ticker.csv',
            'RedisCollectKey': 'binance-XRP_USDT-ticker_raw',
            'RedisOutputKey': 'binance-XRP_USDT-ticker_processed',
            'DataHandler': 'process_trade_data',
        },
    },
}

OkexConfigs = {
    'BTC/USDT': {
        'order': {
            'Subscription': {
                'event': 'addChannel',
                'channel': 'ok_sub_spot_btc_usdt_depth_20',
            },
            'OrderBookDepth': 20,
            'Header': order_book_header_with_depth(20),
            'FileName': 'BTC_USDT-okex.book.csv',
            'RedisCollectKey': 'okex-BTC_USDT-order_raw',
            'RedisOutputKey': 'okex-BTC_USDT-order_processed',
            'DataHandler': 'process_order_data',
            'TickSize': 0.01,
            'AmountMin': 1e-8,
        },

        'trade': {
            'Subscription': {
                'event': 'addChannel',
                'channel': 'ok_sub_spot_btc_usdt_deals',
            },
            'Header': [
                'dealid',
                'price',
                'size',
                'dealtime',
                'side',
            ],
            'FileName': 'BTC_USDT-okex.trade.csv',
            'RedisCollectKey': 'okex-BTC_USDT-trade_raw',
            'RedisOutputKey': 'okex-BTC_USDT-trade_processed',
            'DataHandler': 'process_trade_data',
        },
    },

    'BCH/USDT': {
        'order': {
            'Subscription': {
                'event': 'addChannel',
                'channel': 'ok_sub_spot_bch_usdt_depth_20',
            },
            'OrderBookDepth': 20,
            'Header': order_book_header_with_depth(20),
            'FileName': 'BCH_USDT-okex.book.csv',
            'RedisCollectKey': 'okex-BCH_USDT-order_raw',
            'RedisOutputKey': 'okex-BCH_USDT-order_processed',
            'DataHandler': 'process_order_data',
            'TickSize': 0.01,
            'AmountMin': 1e-8,
        },

        'trade': {
            'Subscription': {
                'event': 'addChannel',
                'channel': 'ok_sub_spot_bch_usdt_deals',
            },
            'Header': [
                'dealid',
                'price',
                'size',
                'dealtime',
                'side',
            ],
            'FileName': 'BCH_USDT-okex.trade.csv',
            'RedisCollectKey': 'okex-BCH_USDT-trade_raw',
            'RedisOutputKey': 'okex-BCH_USDT-trade_processed',
            'DataHandler': 'process_trade_data',
        },
    },

    'ETH/USDT': {
        'order': {
            'Subscription': {
                'event': 'addChannel',
                'channel': 'ok_sub_spot_eth_usdt_depth_20',
            },
            'OrderBookDepth': 20,
            'Header': order_book_header_with_depth(20),
            'FileName': 'ETH_USDT-okex.book.csv',
            'RedisCollectKey': 'okex-ETH_USDT-order_raw',
            'RedisOutputKey': 'okex-ETH_USDT-order_processed',
            'DataHandler': 'process_order_data',
            'TickSize': 0.01,
            'AmountMin': 1e-8,
        },

        'trade': {
            'Subscription': {
                'event': 'addChannel',
                'channel': 'ok_sub_spot_eth_usdt_deals',
            },
            'Header': [
                'dealid',
                'price',
                'size',
                'dealtime',
                'side',
            ],
            'FileName': 'ETH_USDT-okex.trade.csv',
            'RedisCollectKey': 'okex-ETH_USDT-trade_raw',
            'RedisOutputKey': 'okex-ETH_USDT-trade_processed',
            'DataHandler': 'process_trade_data',
        },
    },

    'EOS/USDT': {
        'order': {
            'Subscription': {
                'event': 'addChannel',
                'channel': 'ok_sub_spot_eos_usdt_depth_20',
            },
            'OrderBookDepth': 20,
            'Header': order_book_header_with_depth(20),
            'FileName': 'EOS_USDT-okex.book.csv',
            'RedisCollectKey': 'okex-EOS_USDT-order_raw',
            'RedisOutputKey': 'okex-EOS_USDT-order_processed',
            'DataHandler': 'process_order_data',
            'TickSize': 0.01,
            'AmountMin': 1e-8,
        },

        'trade': {
            'Subscription': {
                'event': 'addChannel',
                'channel': 'ok_sub_spot_eos_usdt_deals',
            },
            'Header': [
                'dealid',
                'price',
                'size',
                'dealtime',
                'side',
            ],
            'FileName': 'EOS_USDT-okex.trade.csv',
            'RedisCollectKey': 'okex-EOS_USDT-trade_raw',
            'RedisOutputKey': 'okex-EOS_USDT-trade_processed',
            'DataHandler': 'process_trade_data',
        },
    },

    'XRP/USDT': {
        'order': {
            'Subscription': {
                'event': 'addChannel',
                'channel': 'ok_sub_spot_xrp_usdt_depth_20',
            },
            'OrderBookDepth': 20,
            'Header': order_book_header_with_depth(20),
            'FileName': 'XRP_USDT-okex.book.csv',
            'RedisCollectKey': 'okex-XRP_USDT-order_raw',
            'RedisOutputKey': 'okex-XRP_USDT-order_processed',
            'DataHandler': 'process_order_data',
            'TickSize': 0.01,
            'AmountMin': 1e-8,
        },

        'trade': {
            'Subscription': {
                'event': 'addChannel',
                'channel': 'ok_sub_spot_xrp_usdt_deals',
            },
            'Header': [
                'dealid',
                'price',
                'size',
                'dealtime',
                'side',
            ],
            'FileName': 'XRP_USDT-okex.trade.csv',
            'RedisCollectKey': 'okex-XRP_USDT-trade_raw',
            'RedisOutputKey': 'okex-XRP_USDT-trade_processed',
            'DataHandler': 'process_trade_data',
        },
    },
}

BitfinexConfigs = {
    'BTC/USD': {
        'trade': {
            'Subscription': {
                'event': 'subscribe',
                'channel': 'trades',
                'symbol': 'tBTCUSD',
            },
            'Header': [
                'type',
                'id',
                'side',
                'amount',
                'price',
            ],
            'FileName': 'BTC_USD-bitfinex.trade.csv',
            'RedisCollectKey': 'bitfinex-BTC_USD-trade_raw',
            'RedisOutputKey': 'bitfinex-BTC_USD-trade_processed',
            'DataHandler': 'process_trade_data',
        },

        'order': {
            'Subscription': {
                'event': 'subscribe',
                'channel': 'book',
                'symbol': 'tBTCUSD',
            },
            'Header': order_book_header_with_depth(20),
            'OrderBookDepth': 20,
            'InitBookDepth': 25,
            'FileName': 'BTC_USD-bitfinex.book.csv',
            'RedisCollectKey': 'bitfinex-BTC_USD-order_raw',
            'RedisOutputKey': 'bitfinex-BTC_USD-order_processed',
            'DataHandler': 'process_order_book_data',
            'TickSize': 0.01,
            'AmountMin': 1e-8,
        },
    },

    'BCH/USD': {
        'trade': {
            'Subscription': {
                'event': 'subscribe',
                'channel': 'trades',
                'symbol': 'tBCHUSD',
            },
            'Header': [
                'type',
                'id',
                'side',
                'amount',
                'price',
            ],
            'FileName': 'BCH_USD-bitfinex.trade.csv',
            'RedisCollectKey': 'bitfinex-BCH_USD-trade_raw',
            'RedisOutputKey': 'bitfinex-BCH_USD-trade_processed',
            'DataHandler': 'process_trade_data',
        },

        'order': {
            'Subscription': {
                'event': 'subscribe',
                'channel': 'book',
                'symbol': 'tBCHUSD',
            },
            'Header': order_book_header_with_depth(20),
            'OrderBookDepth': 20,
            'InitBookDepth': 25,
            'FileName': 'BCH_USD-bitfinex.book.csv',
            'RedisCollectKey': 'bitfinex-BCH_USD-order_raw',
            'RedisOutputKey': 'bitfinex-BCH_USD-order_processed',
            'DataHandler': 'process_order_book_data',
            'TickSize': 0.01,
            'AmountMin': 1e-8,
        },
    },

    'ETH/USD': {
        'trade': {
            'Subscription': {
                'event': 'subscribe',
                'channel': 'trades',
                'symbol': 'tETHUSD',
            },
            'Header': [
                'type',
                'id',
                'side',
                'amount',
                'price',
            ],
            'FileName': 'ETH_USD-bitfinex.trade.csv',
            'RedisCollectKey': 'bitfinex-ETH_USD-trade_raw',
            'RedisOutputKey': 'bitfinex-ETH_USD-trade_processed',
            'DataHandler': 'process_trade_data',
        },

        'order': {
            'Subscription': {
                'event': 'subscribe',
                'channel': 'book',
                'symbol': 'tETHUSD',
            },
            'Header': order_book_header_with_depth(20),
            'OrderBookDepth': 20,
            'InitBookDepth': 25,
            'FileName': 'ETH_USD-bitfinex.book.csv',
            'RedisCollectKey': 'bitfinex-ETH_USD-order_raw',
            'RedisOutputKey': 'bitfinex-ETH_USD-order_processed',
            'DataHandler': 'process_order_book_data',
            'TickSize': 0.01,
            'AmountMin': 1e-8,
        },
    },
}

HitbtcConfigs = {
    'BTC/USD': {
        'trade': {
            'Subscription': {
                "method": "subscribeTrades",
                "params": {
                    "symbol": "BTCUSD"
                },
            },
            'Header': [
                'id',
                'price',
                'quantity',
                'side',
            ],
            'FileName': 'BTC_USD-hitbtc.trade.csv',
            'RedisCollectKey': 'hitbtc-BTC_USD-trade_raw',
            'RedisOutputKey': 'hitbtc-BTC_USD-trade_processed',
            'DataHandler': 'process_trade_data',
        },

        'order': {
            'Subscription': {
                "method": "subscribeOrderbook",
                "params": {
                    "symbol": "BTCUSD"
                },
            },
            'Header': order_book_header_with_depth(12),
            'OrderBookDepth': 12,
            'FileName': 'BTC_USD-hitbtc.book.csv',
            'RedisCollectKey': 'hitbtc-BTC_USD-order_raw',
            'RedisOutputKey': 'hitbtc-BTC_USD-order_processed',
            'DataHandler': 'process_order_data',
            'TickSize': 0.01,
            'AmountMin': 1e-8,
        },
    },

    'BCH/USD': {
        'trade': {
            'Subscription': {
                "method": "subscribeTrades",
                "params": {
                    "symbol": "BCHUSD"
                },
            },
            'Header': [
                'id',
                'price',
                'quantity',
                'side',
            ],
            'FileName': 'BCH_USD-hitbtc.trade.csv',
            'RedisCollectKey': 'hitbtc-BCH_USD-trade_raw',
            'RedisOutputKey': 'hitbtc-BCH_USD-trade_processed',
            'DataHandler': 'process_trade_data',
        },

        'order': {
            'Subscription': {
                "method": "subscribeOrderbook",
                "params": {
                    "symbol": "BCHUSD"
                },
            },
            'Header': order_book_header_with_depth(12),
            'OrderBookDepth': 12,
            'FileName': 'BCH_USD-hitbtc.book.csv',
            'RedisCollectKey': 'hitbtc-BCH_USD-order_raw',
            'RedisOutputKey': 'hitbtc-BCH_USD-order_processed',
            'DataHandler': 'process_order_data',
            'TickSize': 0.01,
            'AmountMin': 1e-8,
        },
    },

    'ETH/USD': {
        'trade': {
            'Subscription': {
                "method": "subscribeTrades",
                "params": {
                    "symbol": "ETHUSD"
                },
            },
            'Header': [
                'id',
                'price',
                'quantity',
                'side',
            ],
            'FileName': 'ETH_USD-hitbtc.trade.csv',
            'RedisCollectKey': 'hitbtc-ETH_USD-trade_raw',
            'RedisOutputKey': 'hitbtc-ETH_USD-trade_processed',
            'DataHandler': 'process_trade_data',
        },

        'order': {
            'Subscription': {
                "method": "subscribeOrderbook",
                "params": {
                    "symbol": "ETHUSD"
                },
            },
            'Header': order_book_header_with_depth(12),
            'OrderBookDepth': 12,
            'FileName': 'ETH_USD-hitbtc.book.csv',
            'RedisCollectKey': 'hitbtc-ETH_USD-order_raw',
            'RedisOutputKey': 'hitbtc-ETH_USD-order_processed',
            'DataHandler': 'process_order_data',
            'TickSize': 0.01,
            'AmountMin': 1e-8,
        },
    },

    'EOS/USD': {
        'trade': {
            'Subscription': {
                "method": "subscribeTrades",
                "params": {
                    "symbol": "EOSUSD"
                },
            },
            'Header': [
                'id',
                'price',
                'quantity',
                'side',
            ],
            'FileName': 'EOS_USD-hitbtc.trade.csv',
            'RedisCollectKey': 'hitbtc-EOS_USD-trade_raw',
            'RedisOutputKey': 'hitbtc-EOS_USD-trade_processed',
            'DataHandler': 'process_trade_data',
        },

        'order': {
            'Subscription': {
                "method": "subscribeOrderbook",
                "params": {
                    "symbol": "EOSUSD"
                },
            },
            'Header': order_book_header_with_depth(12),
            'OrderBookDepth': 12,
            'FileName': 'EOS_USD-hitbtc.book.csv',
            'RedisCollectKey': 'hitbtc-EOS_USD-order_raw',
            'RedisOutputKey': 'hitbtc-EOS_USD-order_processed',
            'DataHandler': 'process_order_data',
            'TickSize': 0.01,
            'AmountMin': 1e-8,
        },
    },

    'XRP/USD': {
        'trade': {
            'Subscription': {
                "method": "subscribeTrades",
                "params": {
                    "symbol": "XRPUSDT"
                },
            },
            'Header': [
                'id',
                'price',
                'quantity',
                'side',
            ],
            'FileName': 'XRP_USD-hitbtc.trade.csv',
            'RedisCollectKey': 'hitbtc-XRP_USD-trade_raw',
            'RedisOutputKey': 'hitbtc-XRP_USD-trade_processed',
            'DataHandler': 'process_trade_data',
        },

        'order': {
            'Subscription': {
                "method": "subscribeOrderbook",
                "params": {
                    "symbol": "XRPUSDT"
                },
            },
            'Header': order_book_header_with_depth(12),
            'OrderBookDepth': 12,
            'FileName': 'XRP_USD-hitbtc.book.csv',
            'RedisCollectKey': 'hitbtc-XRP_USD-order_raw',
            'RedisOutputKey': 'hitbtc-XRP_USD-order_processed',
            'DataHandler': 'process_order_data',
            'TickSize': 0.01,
            'AmountMin': 1e-8,
        },
    },
}

BitstampConfigs = {
    'BTC/USD': {
        'trade': {
            'Subscription': {
                "event": "pusher:subscribe",
                "data": {
                    "channel": "live_trades"
                },
            },
            'Header': [
                'amount',
                'buy_order_id',
                'sell_order_id',
                'amount_str',
                'price_str',
                'type',
                'id',
                'price',
            ],
            'FileName': 'BTC_USD-bitstamp.trade.csv',
            'RedisCollectKey': 'bitstamp-BTC_USD-trade_raw',
            'RedisOutputKey': 'bitstamp-BTC_USD-trade_processed',
            'DataHandler': 'process_trade_data',
        },

        'order': {
            'Subscription': {
                "event": "pusher:subscribe",
                "data": {
                    "channel": "order_book"
                },
            },
            'Header': order_book_header_with_depth(20),
            'OrderBookDepth': 20,
            'FileName': 'BTC_USD-bitstamp.book.csv',
            'RedisCollectKey': 'bitstamp-BTC_USD-order_raw',
            'RedisOutputKey': 'bitstamp-BTC_USD-order_processed',
            'DataHandler': 'process_order_data',
            'TickSize': 0.01,
            'AmountMin': 1e-8,
        },
    },

    'BCH/USD': {
        'trade': {
            'Subscription': {
                "event": "pusher:subscribe",
                "data": {
                    "channel": "live_trades_bchusd"
                },
            },
            'Header': [
                'amount',
                'buy_order_id',
                'sell_order_id',
                'amount_str',
                'price_str',
                'type',
                'id',
                'price',
            ],
            'FileName': 'BCH_USD-bitstamp.trade.csv',
            'RedisCollectKey': 'bitstamp-BCH_USD-trade_raw',
            'RedisOutputKey': 'bitstamp-BCH_USD-trade_processed',
            'DataHandler': 'process_trade_data',
        },

        'order': {
            'Subscription': {
                "event": "pusher:subscribe",
                "data": {
                    "channel": "order_book_bchusd"
                },
            },
            'Header': order_book_header_with_depth(20),
            'OrderBookDepth': 20,
            'FileName': 'BCH_USD-bitstamp.book.csv',
            'RedisCollectKey': 'bitstamp-BCH_USD-order_raw',
            'RedisOutputKey': 'bitstamp-BCH_USD-order_processed',
            'DataHandler': 'process_order_data',
            'TickSize': 0.01,
            'AmountMin': 1e-8,
        },
    },

    'ETH/USD': {
        'trade': {
            'Subscription': {
                "event": "pusher:subscribe",
                "data": {
                    "channel": "live_trades_ethusd"
                },
            },
            'Header': [
                'amount',
                'buy_order_id',
                'sell_order_id',
                'amount_str',
                'price_str',
                'type',
                'id',
                'price',
            ],
            'FileName': 'ETH_USD-bitstamp.trade.csv',
            'RedisCollectKey': 'bitstamp-ETH_USD-trade_raw',
            'RedisOutputKey': 'bitstamp-ETH_USD-trade_processed',
            'DataHandler': 'process_trade_data',
        },

        'order': {
            'Subscription': {
                "event": "pusher:subscribe",
                "data": {
                    "channel": "order_book_ethusd"
                },
            },
            'Header': order_book_header_with_depth(20),
            'OrderBookDepth': 20,
            'FileName': 'ETH_USD-bitstamp.book.csv',
            'RedisCollectKey': 'bitstamp-ETH_USD-order_raw',
            'RedisOutputKey': 'bitstamp-ETH_USD-order_processed',
            'DataHandler': 'process_order_data',
            'TickSize': 0.01,
            'AmountMin': 1e-8,
        },
    },

    'XRP/USD': {
        'trade': {
            'Subscription': {
                "event": "pusher:subscribe",
                "data": {
                    "channel": "live_trades_xrpusd"
                },
            },
            'Header': [
                'amount',
                'buy_order_id',
                'sell_order_id',
                'amount_str',
                'price_str',
                'type',
                'id',
                'price',
            ],
            'FileName': 'XRP_USD-bitstamp.trade.csv',
            'RedisCollectKey': 'bitstamp-XRP_USD-trade_raw',
            'RedisOutputKey': 'bitstamp-XRP_USD-trade_processed',
            'DataHandler': 'process_trade_data',
        },

        'order': {
            'Subscription': {
                "event": "pusher:subscribe",
                "data": {
                    "channel": "order_book_xrpusd"
                },
            },
            'Header': order_book_header_with_depth(20),
            'OrderBookDepth': 20,
            'FileName': 'XRP_USD-bitstamp.book.csv',
            'RedisCollectKey': 'bitstamp-XRP_USD-order_raw',
            'RedisOutputKey': 'bitstamp-XRP_USD-order_processed',
            'DataHandler': 'process_order_data',
            'TickSize': 0.01,
            'AmountMin': 1e-8,
        },
    },
}

ZbConfigs = {
    'BTC/USDT': {
        'trade': {
            'Subscription': {
                'event': 'addChannel',
                'channel': 'btcusdt_trades',
            },
            'Header': [
                'amount',
                'price',
                'tid',
                'type',
                'trade_type',
            ],
            'FileName': 'BTC_USDT-zb.trade.csv',
            'RedisCollectKey': 'zb-BTC_USDT-trade_raw',
            'RedisOutputKey': 'zb-BTC_USDT-trade_processed',
            'DataHandler': 'process_trade_data',
        },

        'order': {
            'Subscription': {
                'event': 'addChannel',
                'channel': 'btcusdt_depth',
            },
            'Header': order_book_header_with_depth(20),
            'OrderBookDepth': 20,
            'FileName': 'BTC_USDT-zb.book.csv',
            'RedisCollectKey': 'zb-BTC_USDT-order_raw',
            'RedisOutputKey': 'zb-BTC_USDT-order_processed',
            'DataHandler': 'process_order_data',
            'TickSize': 0.01,
            'AmountMin': 1e-8,
        },
    },

    'ETH/USDT': {
        'trade': {
            'Subscription': {
                'event': 'addChannel',
                'channel': 'ethusdt_trades',
            },
            'Header': [
                'amount',
                'price',
                'tid',
                'type',
                'trade_type',
            ],
            'FileName': 'ETH_USDT-zb.trade.csv',
            'RedisCollectKey': 'zb-ETH_USDT-trade_raw',
            'RedisOutputKey': 'zb-ETH_USDT-trade_processed',
            'DataHandler': 'process_trade_data',
        },

        'order': {
            'Subscription': {
                'event': 'addChannel',
                'channel': 'ethusdt_depth',
            },
            'Header': order_book_header_with_depth(20),
            'OrderBookDepth': 20,
            'FileName': 'ETH_USDT-zb.book.csv',
            'RedisCollectKey': 'zb-ETH_USDT-order_raw',
            'RedisOutputKey': 'zb-ETH_USDT-order_processed',
            'DataHandler': 'process_order_data',
            'TickSize': 0.01,
            'AmountMin': 1e-8,
        },
    },

    'BCH/USDT': {
        'trade': {
            'Subscription': {
                'event': 'addChannel',
                'channel': 'bccusdt_trades',
            },
            'Header': [
                'amount',
                'price',
                'tid',
                'type',
                'trade_type',
            ],
            'FileName': 'BCH_USDT-zb.trade.csv',
            'RedisCollectKey': 'zb-BCH_USDT-trade_raw',
            'RedisOutputKey': 'zb-BCH_USDT-trade_processed',
            'DataHandler': 'process_trade_data',
        },

        'order': {
            'Subscription': {
                'event': 'addChannel',
                'channel': 'bccusdt_depth',
            },
            'Header': order_book_header_with_depth(20),
            'OrderBookDepth': 20,
            'FileName': 'BCH_USDT-zb.book.csv',
            'RedisCollectKey': 'zb-BCH_USDT-order_raw',
            'RedisOutputKey': 'zb-BCH_USDT-order_processed',
            'DataHandler': 'process_order_data',
            'TickSize': 0.01,
            'AmountMin': 1e-8,
        },
    },

    'EOS/USDT': {
        'trade': {
            'Subscription': {
                'event': 'addChannel',
                'channel': 'eosusdt_trades',
            },
            'Header': [
                'amount',
                'price',
                'tid',
                'type',
                'trade_type',
            ],
            'FileName': 'EOS_USDT-zb.trade.csv',
            'RedisCollectKey': 'zb-EOS_USDT-trade_raw',
            'RedisOutputKey': 'zb-EOS_USDT-trade_processed',
            'DataHandler': 'process_trade_data',
        },

        'order': {
            'Subscription': {
                'event': 'addChannel',
                'channel': 'eosusdt_depth',
            },
            'Header': order_book_header_with_depth(20),
            'OrderBookDepth': 20,
            'FileName': 'EOS_USDT-zb.book.csv',
            'RedisCollectKey': 'zb-EOS_USDT-order_raw',
            'RedisOutputKey': 'zb-EOS_USDT-order_processed',
            'DataHandler': 'process_order_data',
            'TickSize': 0.01,
            'AmountMin': 1e-8,
        },
    },

    'XRP/USDT': {
        'trade': {
            'Subscription': {
                'event': 'addChannel',
                'channel': 'xrpusdt_trades',
            },
            'Header': [
                'amount',
                'price',
                'tid',
                'type',
                'trade_type',
            ],
            'FileName': 'XRP_USDT-zb.trade.csv',
            'RedisCollectKey': 'zb-XRP_USDT-trade_raw',
            'RedisOutputKey': 'zb-XRP_USDT-trade_processed',
            'DataHandler': 'process_trade_data',
        },

        'order': {
            'Subscription': {
                'event': 'addChannel',
                'channel': 'xrpusdt_depth',
            },
            'Header': order_book_header_with_depth(20),
            'OrderBookDepth': 20,
            'FileName': 'XRP_USDT-zb.book.csv',
            'RedisCollectKey': 'zb-XRP_USDT-order_raw',
            'RedisOutputKey': 'zb-XRP_USDT-order_processed',
            'DataHandler': 'process_order_data',
            'TickSize': 0.01,
            'AmountMin': 1e-8,
        },
    },
}

ExConfigs = {
    'Gdax': [GdaxConfigs, 'wss://ws-feed.gdax.com'],
    'Huobipro': [HuobiConfigs, 'wss://api.huobipro.com/ws'],
    'Gemini': [GeminiConfigs, 'wss://api.gemini.com/v1/'],
    'Bitmex': [BitmexConfigs, 'wss://www.bitmex.com/realtime'],
    'Binance': [BinanceConfigs, 'wss://stream.binance.com:9443'],
    'Okex': [OkexConfigs, 'wss://real.okex.com:10441/websocket'],
    'Bitfinex': [BitfinexConfigs, 'wss://api.bitfinex.com/ws/2'],
    'Hitbtc': [HitbtcConfigs, 'wss://api.hitbtc.com/api/2/ws'],
    'Bitstamp': [BitstampConfigs, 'wss://ws.pusherapp.com:443/app/de504dc5763aeef9'
                                  'ff52?client=PythonPusherClient&version=0.2.0&protocol=6'],
    'Zb': [ZbConfigs, 'wss://api.zb.cn:9999/websocket']
}
