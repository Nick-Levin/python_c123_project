import uuid
import time
import random
from event import Event


def generate_random_event():
    event_id = uuid.uuid4()
    return Event(
        str(event_id),
        time.time(),
        str(uuid.uuid4()),
        random.randint(100, 500),
        "msg - " + str(event_id)
    )
