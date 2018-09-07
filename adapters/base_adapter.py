#coding=utf-8

import abc

class PushAdapter:
    __metaclass__ = abc.ABCMeta

    def __init__(self, exchange_id):
        self.exchange_id = exchange_id
        return

    @abc.abstractmethod
    def push(self, msg):
        pass


