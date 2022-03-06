from src.logger import Logger


from src.logger import Logger
from datetime import date, datetime

class PVPC:
    _date = None
    _max = None
    _min = None

    def __init__(self, json):
        Logger().info("New PVPC item")
        if 'PVPC' not in json: raise Exception('Invalid JSON object for PVPC')
        if len(json['PVPC']) != 24: raise Exception('Invalid number of items in PVPC object')
        self._json = json

    def date(self):
        if (self._date == None):
            self._date = datetime.strptime(str(self._json['PVPC'][0]['Dia']), '%d/%m/%Y')
        return self._date
    
    def max(self):
        if (self._max == None):
            self._max = max(self._json['PVPC'], key=lambda item: float(item['PCB'].replace(',','.')))
        return self._max['PCB']

    def min(self):
        if (self._min == None):
            self._min = min(self._json['PVPC'], key=lambda item: float(item['PCB'].replace(',','.')))
        return self._min['PCB']