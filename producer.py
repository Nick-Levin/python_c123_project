from kafka import KafkaProducer
from event_generator import generate_random_event
import json

if __name__ == '__main__':
    kafka_producer = KafkaProducer(bootstrap_servers='localhost:9092')  # hibur le kafka

    for i in range(500):
        event = generate_random_event() #generazia shel random event
        json_event = json.dumps(event.__dict__) #ofeh et event le json #dict ze kmo obejct object=dict
        kafka_producer.send(topic='test', value=json_event.encode()) #omer le producer lidhof et a value le toh a tor tor=topic

        #consumer=mosheh me a tor  /     producer=dohef la tor       tor=topic
