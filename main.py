#!/usr/bin/python3

from src.logger import Logger
from src.pvpc import PVPC
import json
import requests
from datetime import datetime, date, timedelta

def main():
    log = Logger()
    log.start("ree.log")
    try:
        log.info('Hello world')
        it_date = date(2022, 1, 1)
        end_date = date(2022, 3, 6)
        delta = timedelta(days=1)
        while it_date <= end_date:
            # TODO: cache info
            url = 'https://api.esios.ree.es/archives/70/download_json?locale=es&date={}-{}-{}'.format(it_date.year, it_date.month, it_date.day)
            p = PVPC(json.loads(requests.get(url).text))
            log.info(p.date().strftime("%Y-%m-%d"))
            log.info('Max: ' + p.max())
            log.info('Min: ' + p.min())
            it_date += delta
    except Exception as e:
        log.error(str(e))
    log.stop()

if __name__== "__main__":
    main()
