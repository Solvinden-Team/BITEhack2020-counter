import json
import random

from camera_reader import Reader
from counter import Counter
from time import sleep, time
import requests


def main():
    url = 'http://localhost:8080/count/{}'
    sleep_time = 10
    reader = Reader()
    counter = Counter()
    headers = {"Content-type": 'application/json'}
    while True:
        img = reader.read()
        cnt = counter.count(img)
        timestamp = int(time() * 1000)
        content = {
            "timestamp": timestamp,
            "peopleCount": cnt
        }
        requests.post(url.format(3), data=json.dumps(content), headers=headers)
        sleep(sleep_time)


if __name__ == "__main__":
    main()
