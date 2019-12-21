import requests
from concurrent import futures
from functools import wraps
from functools import wraps
from time import time
import timeit

NUMBER_OF_REQUESTS = 20


def timing(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        print('Elapsed time: {}'.format(end-start))
        return result
    return wrapper


def download_one():
    response = requests.get('http://adrianov.pro')
    print(response.status_code)


@timing
def simple_request():
    for _ in range(0, NUMBER_OF_REQUESTS):
        download_one()


@timing
def concurrent_request():
    ll = [_ for _ in range(0, NUMBER_OF_REQUESTS)]
    with futures.ThreadPoolExecutor(NUMBER_OF_REQUESTS) as executor:
        executor.map(download_one, ll)


simple_request()
