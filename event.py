
class Event:
    # constructor
    def __init__(self, reporter_id, timestamp, metric_id, metric_value, message):
        self.reporter_id = reporter_id
        self.timestamp = timestamp
        self.metric_id = metric_id
        self.metric_value = metric_value
        self.message = message

    def __str__(self):
        return f'reporter_id = {self.reporter_id}\ntimestamp = {self.timestamp}\nmetric_id = {self.metric_id}\n' \
               f'metric_value = {self.metric_value}\nmessage = {self.message}'
