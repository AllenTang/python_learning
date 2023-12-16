import requests
from loguru import logger
import json


def fetch_main_page():
    proxies = {
        'http': 'http://localhost:7890',
        'https': 'http://localhost:7890',
    }
    url = 'https://bbs.qzzn.com/forum-29-1.html'
    logger.info('starting')
    resp = requests.get(url, proxies=proxies)
    logger.info('resp: {}', resp.text)

