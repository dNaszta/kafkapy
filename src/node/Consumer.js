var kafka = require('kafka-node'),
Consumer = kafka.Consumer,
client = new kafka.KafkaClient('kafka:9094'),
consumer = new Consumer(
    client,
    [
        { topic: 'test', partition: 0 }
    ],
    {
        autoCommit: false
    }
);

consumer.on('message', function(message) {
  console.log(message);
})