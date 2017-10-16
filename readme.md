#Install working example
    1. sudo apt install python3-pip
    2. pip3 install virtualenv
    3. python3 -m virtualenv kafka
    4. cd kafka
    5. source bin/activate
    6. pip install -r requirements.txt
    7. install (min) Docker version 17.09.0-ce and (min) docker-compose version 1.16.1
    8. cd kafka-docker
    9. docker-compose -f docker-compose-single-broker.yml up
    10. add /etc/hosts kafka 127.0.0.1 
    11. use python <i>src/producer.py</i> for produce
    12. use python <i>src/consumer.py</i> as many as you want

#Install php producer
    1. Make sure if you have installed librdkafka-dev_0.11.0-1_i386.deb from https://launchpad.net/ubuntu/+source/librdkafka
    2. sudo apt-get install re2c
    3. sudo pecl install rdkafka
    4. set extension=rdkafka.so in php.ini
    5. now you can run php producer.php to test producer