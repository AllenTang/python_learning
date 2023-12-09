import requests
from loguru import logger
import json


def fetch_main_page():
    proxies = {
        'http': 'http://localhost:7890',
        'https': 'http://localhost:7890',
    }
    url = 'https://click.suning.cn/sa/jsConfig.action?dm=list.suning.com'
    logger.info('starting')
    resp = requests.get(url, proxies=proxies)
    logger.info('resp: {}', resp.text)
    obj = json.loads(resp.text)
    logger.info('resp: {}', obj.keys())

