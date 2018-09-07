#coding=utf-8                         

import json

from pykafka import KafkaClient

from hftcoin.mdagent.adapters.base_adapter import PushAdapter
from hftcoin.commons.kafka_configs import KafkaConfigs
                  
class KafkaPushAdapter(PushAdapter):

    client = KafkaClient(hosts=KafkaConfigs.get('kafka_hosts'), zookeeper_hosts=KafkaConfigs.get('zookeeper_hosts'))

    def __init__(self, exchange_id):
        super(KafkaPushAdapter, self).__init__(exchange_id)

        self.topic_name = exchange_id + '_order'
        self.topic = self.client.topics[self.topic_name.encode()]
        self.producer = self.topic.get_producer(sync=True)
        return
        
    def push(self, msg):
        msg = json.dumps(msg).encode()
        self.producer.produce(msg)
        return 

    def __del__(self):
        self.producer.stop()
        return
