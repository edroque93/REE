from datetime import datetime, timedelta
import json

from src.web import web

class pvpc:
    _date = None
    _max = None
    _min = None
    _avg = None

    def __init__(self, json):
        if 'PVPC' not in json: raise Exception('Invalid JSON object for PVPC')
        self._hours = len(json['PVPC'])
        if self._hours < 23 or self._hours > 25: raise Exception('Invalid number of items in PVPC object')
        self._json = json
        self._tag = 'PCB' if 'PCB' in json['PVPC'][0] else 'GEN'

    def date(self):
        if (self._date == None):
            self._date = datetime.strptime(str(self._json['PVPC'][0]['Dia']), '%d/%m/%Y')
        return self._date
    
    def max(self):
        if (self._max == None):
            self._max = max(self._json['PVPC'], key=lambda item: float(item[self._tag].replace(',','.')))
        return float(self._max[self._tag].replace(',','.'))

    def min(self):
        if (self._min == None):
            self._min = min(self._json['PVPC'], key=lambda item: float(item[self._tag].replace(',','.')))
        return float(self._min[self._tag].replace(',','.'))

    def avg(self):
        if (self._avg == None):
            self._avg = round(sum(map(lambda item: float(item[self._tag].replace(',','.')), self._json['PVPC'])) / self._hours, 2)
        return self._avg
    
    def fetch(date_start, date_end):
        it_date = date_start
        delta = timedelta(days=1)
        request = web('.cache')
        collection = []
        while it_date <= date_end:
            url = 'https://api.esios.ree.es/archives/70/download_json?locale=es&date={}-{}-{}'.format(it_date.year, it_date.month, it_date.day)
            it_date += delta
            data = request.get(url)
            try:
                p = pvpc(json.loads(data))
            except:
                data = request.get(url, True)
                p = pvpc(json.loads(data))
            collection.append(p)
        return collection
