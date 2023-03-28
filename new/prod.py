from kafka import KafkaProducer
import json
from data import get_registered_user
import time


def get_partition(key, all, available):
    #return 0 entails persist message to P0
    return 0

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                         partitioner=get_partition
                        )

if __name__ == '__main__':
    while 1 == 1:
        registered_user = get_registered_user()
        producer.send('test-events', registered_user)
        print(registered_user)
        time.sleep(4)




