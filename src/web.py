from src.logger import logger

import os.path
import requests
import json

class web:
    _instance = None
    _cache = None
    _cacheFile = None

    def __init__(self, cache):
        logger().info('Using web cache "{}"'.format(cache))
        self._cacheFile = cache
        if os.path.exists(cache):
            f = open(cache, 'r')
            self._cache = json.load(f)
            f.close()
    
    def __del__(self):
        f = open(self._cacheFile, 'w')
        json.dump(self._cache, f)
        f.close()

    def get(self, url, force = False):
        if self._cache == None:
            self._cache = {}
        if not force and url in self._cache:
            logger().info('CACHE {}'.format(url))
            return self._cache[url]
        else:
            logger().info('GET {}'.format(url))
            req = requests.get(url)
            if req.status_code == 200:
                data = req.text
                self._cache[url] = data
                return data
            raise Exception('Cannot fetch {}'.format(url))
