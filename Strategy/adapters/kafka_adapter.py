#coding=utf-8                         

import json

from pykafka import KafkaClient, common

from hftcoin.commons.kafka_configs import KafkaConfigs
from hftcoin.mdagent.Strategy.adapters.base_adapter import PopAdapter

class KafkaPopAdapter(PopAdapter):
    client = KafkaClient(hosts=KafkaConfigs.get('kafka_hosts'), zookeeper_hosts=KafkaConfigs.get('zookeeper_hosts'))

    def __init__(self, process_id):
        super(KafkaPopAdapter, self).__init__(process_id)

        market_groups = self.config['market_groups']
        iid_groups = self.config['iid_groups']
        union_iid = list(set(market_groups).union(set(iid_groups)))
            
        self.topic_name = []
        self.consumers = []


        for iid in union_iid:
            self.topic_name.append('%s_order' % self.id_clerk.iid_to_exchange_sid(iid))

        for topic_name in self.topic_name:
            topic = self.client.topics[topic_name.encode()]
            consumer_group_name = str(self.process_id)
            consumer = topic.get_balanced_consumer(consumer_group_name.encode(), auto_commit_enable=True, auto_offset_reset=common.OffsetType.LATEST, 
                    reset_offset_on_start=True)
            self.consumers.append([topic, consumer])
        return

    def recv_msg(self): 
        msg_list = []
        for topic, consumer in self.consumers:
            topic_last_offset = topic.latest_available_offsets()[0][0][0] - 1
            consumer_offset = consumer.held_offsets[0]
            while topic_last_offset >= 0 and consumer_offset < topic_last_offset:
                consumer_offset = consumer_offset + 1
                msg = json.loads(consumer.consume().value.decode())
                msg_list.append(msg)
        return msg_list

    def __del__(self):
        for topic, consumer in self.consumers:
            consumer.stop()
        return

def main():
    pop = KafkaPopAdapter('p001')
    pop.recv_msg()

if __name__ == '__main__':
    main()
