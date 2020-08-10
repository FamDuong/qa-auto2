from kafka import KafkaConsumer
from json import loads

from config.environment import COCCOC_NEW_FEED_KAFKA_SERVERS
from config.environment import COCCOC_NEW_FEED_KAFKA_SASL_MECHANISM
from config.environment import COCCOC_NEW_FEED_KAFKA_SASL_PLAIN_USERNAME
from config.environment import COCCOC_NEW_FEED_KAFKA_SASL_PLAIN_PASSWORD
from config.environment import COCCOC_NEW_FEED_KAFKA_SERCURITY_PROTOCOL

class NewsFeedKafka:

    # Get message from Kafka
    # Document: https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html
    def get_kafka_messsage(self, topic, consumer_timeout_ms = 10000):
        consumer = KafkaConsumer(topic,
                                 bootstrap_servers=COCCOC_NEW_FEED_KAFKA_SERVERS,
                                 sasl_mechanism=COCCOC_NEW_FEED_KAFKA_SASL_MECHANISM,
                                 sasl_plain_username=COCCOC_NEW_FEED_KAFKA_SASL_PLAIN_USERNAME,
                                 sasl_plain_password=COCCOC_NEW_FEED_KAFKA_SASL_PLAIN_PASSWORD,
                                 security_protocol=COCCOC_NEW_FEED_KAFKA_SERCURITY_PROTOCOL,
                                 auto_offset_reset="earliest",
                                 enable_auto_commit=False,
                                 value_deserializer=lambda x: loads(x.decode('utf-8')),
                                 consumer_timeout_ms=consumer_timeout_ms)
        list_message = []
        for message in consumer:
            # message value and key are raw bytes -- decode if necessary!
            # e.g., for unicode: `message.value.decode('utf-8')`
            print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                                 message.offset, message.key,
                                                 message.value))
            list_message.append(message)
        return list_message