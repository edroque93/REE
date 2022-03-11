#!/usr/bin/python3

from src.logger import logger
from src.pvpc import pvpc
from src.web import web
import json
from datetime import date, timedelta

def main():
    log = logger()
    log.start("ree.log", False)
    try:
        request = web('.cache')
        it_date = date(2021, 6, 1)
        end_date = date(2022, 3, 11)
        delta = timedelta(days=1)
        print('date;max;avg;min')
        while it_date <= end_date:
            url = 'https://api.esios.ree.es/archives/70/download_json?locale=es&date={}-{}-{}'.format(it_date.year, it_date.month, it_date.day)
            it_date += delta
            data = request.get(url)
            try:
                p = pvpc(json.loads(data))
            except:
                data = request.get(url, True)
                p = pvpc(json.loads(data))
            print('{};{};{};{}'.format(p.date().strftime("%d/%m/%Y"), p.max(), p.avg(), p.min()))
    except Exception as e:
        log.error(str(e))
    log.stop()

if __name__== "__main__":
    main()
