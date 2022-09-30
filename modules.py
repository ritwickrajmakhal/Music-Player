# All features will be written here
from datetime import datetime
from datetime import timedelta

def sleep_time(time):
    # write your code here
    time = int(time)
    current_time = datetime.now()
    future_time = current_time + timedelta(minutes=time)
    return future_time