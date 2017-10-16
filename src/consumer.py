from kafka import KafkaConsumer

topic = "test"

# Subscribe to a regex topic pattern
consumer = KafkaConsumer(
    topic,
    bootstrap_servers=['kafka:9092']
    #client_id='stylers-kafka-01'
)

for message in consumer:
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                         message.offset, message.key,
                                         message.value))
