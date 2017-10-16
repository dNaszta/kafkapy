<?php
/**
 * Code based on: https://github.com/arnaud-lb/php-rdkafka#installation
 * Dependencies
 * extension=rdkafka.so
 * To install use:
 * https://arnaud-lb.github.io/php-rdkafka/phpdoc/rdkafka.installation.pecl.html
 * https://packages.ubuntu.com/search?keywords=re2c
 * https://launchpad.net/ubuntu/+source/librdkafka
 */

$rk = new RdKafka\Producer();
$rk->setLogLevel(LOG_DEBUG);
$rk->addBrokers("127.0.0.1");

$topic = $rk->newTopic("test");

for ($i = 0; $i < 10; $i++) {
    $topic->produce(RD_KAFKA_PARTITION_UA, 0, "Message $i");
    $rk->poll(0);
}

while ($rk->getOutQLen() > 0) {
    $rk->poll(50);
}