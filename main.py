#!/usr/bin/python3

from src.logger import logger
from src.processors import *
from src.pvpc import pvpc
from datetime import date

def main():
    log = logger()
    log.start("ree.log", False)
    try:
        data = pvpc.fetch(date(2014, 4, 1), date(2022, 3, 17))
        # plot_maxweekly(data)
        # print_csv(data)
        plot_limits(data)
    except Exception as e:
        log.error(str(e))
    log.stop()

if __name__== "__main__":
    main()
