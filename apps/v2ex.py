import requests
from loguru import logger


def fetch_main_page():
    proxies = {
        'http': 'http://localhost:7890',
        'https': 'http://localhost:7890',
    }
    url = 'https://www.scrapingbee.com/'
    logger.info('starting')
    resp = requests.get(url, proxies=proxies)
    logger.info('resp: {}', resp.text)
