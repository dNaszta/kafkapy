from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(bootstrap_servers=['kafka:9092'])

topic = "test"

print(producer)
# Asynchronous by default
future = producer.send(topic=topic, key=b'foo', value=b'megyez')
print(future)
try:
    a = 1
    record_metadata = future.get(timeout=60)
    # Successful result returns assigned partition and offset
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)
except KafkaError as e:
    print(e)


