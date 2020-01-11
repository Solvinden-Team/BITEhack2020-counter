import json

from camera_reader import Reader
from counter import Counter
from time import sleep, time
import requests


def main():
    url = 'localhost:8080/count/{}'
    sleep_time = 10
    reader = Reader()
    counter = Counter()
    while True:
        img = reader.read()
        cnt = counter.count(img)
        timestamp = int(time() * 1000)
        content = {
            "timestamp": timestamp,
            "peopleCount": cnt
        }
        requests.post(url.format(1), data=json.dumps(content))
        sleep(sleep_time)


if __name__ == "__main__":
    main()
