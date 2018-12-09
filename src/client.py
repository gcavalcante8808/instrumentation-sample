import requests
import asyncio
import os
import pandas as pd
import json
import random

from collections import Counter


SERVER_PORT = os.getenv('SERVER_PORT', 5000)

url = 'http://localhost:{}/products'.format(SERVER_PORT)

enterprises = (1,2,3,4,5)
products = ['DDR4 Memory', 'DDR3 Memory', 'Intel CPU', 'AMD CPU']

execution_time = list()
execution_results = list()
async def create_product():
    headers = {'Content-Type':'application/json'}
    data = {'name': random.choice(products), 'enterprise_id':random.choice(enterprises),
            'price': random.choice(range(100,200)), 'currency': 'us_dollar'}

    response = requests.post(url, data=json.dumps(data), headers=headers)

    assert response.status_code, 201
    print(data)
    execution_time.append(response.elapsed.total_seconds())
    execution_results.append(response.text)

async def main(loop):
    tasks = [create_product() for i in range(20)]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    print("#### Create Product Routine ###")
    print(Counter(execution_results))
    s = pd.Series(execution_time)
    print(s.describe())

    response = requests.get(url)
    print("#### List all Products Routine:{} ####".format(response.elapsed.total_seconds()))
