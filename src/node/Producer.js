const kafka = require('kafka-node');
const Producer = kafka.Producer;
const client = new kafka.KafkaClient('kafka:9094');
const producer = new Producer(client);

payloads = [
    { topic: 'test', messages: 'hi'}
];

producer.on('ready', function () {
    
    producer.send(payloads, function (err, data) {
        console.log(data);
    });
}).on('error', function (err) {
    console.log(err);
})