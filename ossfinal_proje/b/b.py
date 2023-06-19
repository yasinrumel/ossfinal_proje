from kafka import KafkaConsumer

consumer = KafkaConsumer('orn_mssg', bootstrap_servers='kafka:9075')

for message in consumer:
    print("Yeni bir belge alındı!")
    print(message.value.decode('utf-8'))
