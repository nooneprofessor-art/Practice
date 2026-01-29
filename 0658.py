from datetime import datetime
from time import sleep

while True:
    now = datetime.now()
    print(now.strftime("%H:%M:%S"))
    sleep(1)