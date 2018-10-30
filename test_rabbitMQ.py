import pika

# create connect
'''
If we wanted to connect to a broker on a different machine we'd simply specify its name or IP address here.
'''

# real
ad = "****"
password = "****"
que="foo"
data="test data"


cred = pika.PlainCredentials(ad, password)
# socket_timeout 10000 seconds
params = pika.ConnectionParameters(
    host='127.0.0.1',
    virtual_host='/',
    # port=5672,
    credentials=cred,
    socket_timeout=10000)

connection = pika.BlockingConnection(params)
channel = connection.channel()
# create a queue
channel.queue_declare(queue=que, durable=True)
# send message
'''
route_key=message queue
'''
channel.basic_publish(
    exchange='',
    routing_key=que,
    body=str(data).replace("'", '"'),
    properties=pika.BasicProperties(delivery_mode=2, ))

# print('sent', str(data).replace("'", '"'))
# print("send198")
connection.close()