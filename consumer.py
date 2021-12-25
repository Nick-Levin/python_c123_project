import json
from kafka import KafkaConsumer
import mongo_connection

if __name__ == '__main__':
    events_collection = mongo_connection.get_events_collection()
    consumer = KafkaConsumer(bootstrap_servers='localhost:9092', auto_offset_reset='earliest')
    consumer.subscribe(['test'])

    while True:
        json_event = next(consumer).value.decode() # shoelf et a value ve ofeh oto me bytim le string me kafka
        dict_event = json.loads(json_event)# ofeh oto le python
        events_collection.insert_one(dict_event) #dohef event ehad le mongo
