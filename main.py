import time

import requests

while True:
    print(requests.get("https://www.baidu.com").status_code)
    time.sleep(2)