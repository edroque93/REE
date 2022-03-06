from datetime import datetime

class Logger:
    _instance = None
    _logHandle = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance
    
    def stop(self):
        self.info('Closing log')
        if self._logHandle and not self._logHandle.closed:
            self._logHandle.close()
            self._logHandle = None

    def start(self, fileName):
        self._logHandle = open(fileName, 'a+', 1)
        self.info("Log start")
    
    def info(self, message):
        self.log('INFO', message)

    def error(self, message):
        self.log('ERROR', message)
    
    def log(self, tag, message):
        output = self._getTimeFormatted() + '\t[' + tag + '] ' + message
        print(output)
        if self._logHandle:
            self._logHandle.write(output + '\n')

    def _getTimeFormatted(self):
        now = datetime.now()
        return now.strftime('%Y-%m-%d %H:%M:%S') + '.%02d' % (now.microsecond / 10000)
