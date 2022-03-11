from datetime import datetime

class logger:
    _instance = None
    _logHandle = None
    _stdout = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(logger, cls).__new__(cls)
        return cls._instance
    
    def stop(self):
        self.info('Closing log')
        if self._logHandle and not self._logHandle.closed:
            self._logHandle.close()
            self._logHandle = None

    def start(self, fileName, stdout):
        self._stdout = stdout
        self._logHandle = open(fileName, 'a+', 1)
        self.info("Log start")
    
    def info(self, message):
        self.log('INFO', message)

    def error(self, message):
        self.log('ERROR', message)
    
    def log(self, tag, message):
        output = self._getTimeFormatted() + '\t[' + tag + '] ' + message
        if (self._stdout): print(output)
        if self._logHandle: self._logHandle.write(output + '\n')

    def _getTimeFormatted(self):
        now = datetime.now()
        return now.strftime('%Y-%m-%d %H:%M:%S') + '.%02d' % (now.microsecond / 10000)
