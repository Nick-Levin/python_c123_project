import json
import time

from mongo_connection import get_events_collection
from bson import ObjectId
import redis
import datetime


def convert_event_to_serializable(event):
    event['timestamp'] = str(datetime.datetime.fromtimestamp(event['timestamp']))
    event['_id'] = str(event['_id'])


if __name__ == '__main__':
    events_collection = get_events_collection()  # tithaber le mongo
    r = redis.Redis(host='localhost', port=6379, db=0) # mithaber le redis

    while True:
        event_last_id = r.get('event_last_id') #tiakh et ha last id me redis
        find_filter = {} # mathil lefaltel

        if event_last_id is None:
            find_filter = {} #mefalter filtur rek (lemashal kshe rak efalta et a sherut ve en sham klum)
        else:
            find_filter = {'_id': {'$gt': ObjectId(event_last_id.decode())}} #ose filtur shel last id gadol me a id a aharon

        result = events_collection.find(find_filter).sort('{"_id": 1}') # ve gam mesader odo im sort me a katan la gadol

        for event in result:
            convert_event_to_serializable(event) #kol event she yesh li ba result ofeh oto le serialiizable
            event_key = str(event['reporter_id']) + ':' + event['timestamp'] #markiv et a key bishvil redis
            event_value = json.dumps(event)#ofeh et a event le json

            r.set('event_last_id', event['_id'])#meadken et a event lasat id
            r.set(event_key, event_value) #dohef et a event le redis

        time.sleep(30)# be siyum a lulaa ea eyn sofit ha sherut ose sleep le 30 shniyot
