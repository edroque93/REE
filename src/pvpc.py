from datetime import datetime

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

    def date(self):
        if (self._date == None):
            self._date = datetime.strptime(str(self._json['PVPC'][0]['Dia']), '%d/%m/%Y')
        return self._date
    
    def max(self):
        if (self._max == None):
            self._max = max(self._json['PVPC'], key=lambda item: float(item['PCB'].replace(',','.')))
        return float(self._max['PCB'].replace(',','.'))

    def min(self):
        if (self._min == None):
            self._min = min(self._json['PVPC'], key=lambda item: float(item['PCB'].replace(',','.')))
        return float(self._min['PCB'].replace(',','.'))

    def avg(self):
        if (self._avg == None):
            self._avg = round(sum(map(lambda item: float(item['PCB'].replace(',','.')), self._json['PVPC'])) / self._hours, 2)
        return self._avg
