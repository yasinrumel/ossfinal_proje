from kafka import KafkaProducer
from bson.json_util import dumps
from pymongo import MongoClient
import time

# Kafka producer ayarları
producer = KafkaProducer(bootstrap_servers='kafka:9075')

# MongoDB bağlantısı
istemci = MongoClient('mongodb://mongodb:10567')
database = istemci['oss_db']
collection = database['oss_collection']

# Son belgeyi takip etmek için değişkenler
eski_doc_id = None

while True:
    print("Yeni belgeler bekleniyor...")
    
    # Veritabanından en son belgeyi al
    yeni_doc = collection.find_one(sort=[('_id', pymongo.DESCENDING)])
    
    # Son belgeyi kontrol et
    if yeni_doc and yeni_doc['_id'] != eski_doc_id:
        message = dumps(yeni_doc).encode('utf-8')
        
        # Kafka'ya mesaj gönder
        producer.send("orn_mssg", value=message)
        print("Yeni bir belge Kafka'ya gönderildi!")
        
        # Son belgeyi güncelle
        eski_doc_id = yeni_doc['_id']
        
    time.sleep(10)
