#coding=utf-8

import abc
import json

from hftcoin.commons.clerk import PathClerk
from hftcoin.commons.clerk import IdClerk


class PopAdapter:
    __metaclass__ = abc.ABCMeta

    def __init__(self, process_id):
        self.id_clerk = IdClerk()
        self.process_id = process_id

        with open('%s/config.json' % PathClerk().config_path(), 'r') as config_file:
            self.config = json.load(config_file)[process_id]

    @abc.abstractmethod
    def recv_msg(self):
        pass

