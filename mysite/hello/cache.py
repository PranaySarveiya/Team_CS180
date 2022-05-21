import logging
from multipledispatch import dispatch

class Cache:
    def __init__(self):
        self.AccidentsCache = {}

    def search(self, name: str) -> str:
        """
        Searches cache for # of accidents in inputted state/city name

        Parameters:
        name (str): name of city/state
        """
        try:
            return self.AccidentsCache.get(name)
        except Exception as e:
            logging.error(e)
    
    @dispatch(str, int)
    def add(self, name: str, cnt: int) -> None:
        """
        Adds city/state to cache with its number of accidents

        Parameters:
        name (str): name of city/state to be inserted into cache
        cnt (int): corresponding # of accidents
        """
        try:
            if(self.AccidentsCache.get(name) == None):
                self.AccidentsCache[name] = cnt
            else:
                self.AccidentsCache[name] += 1
        except Exception as e:
            logging.error(e)

    @dispatch(str, str)
    def add(self, state_name: str, city_name: str) -> None:
        """
        adds 1 city/state accident to the cache
        used for insert statement
        state_name: state of the accident
        city: city of the accident
        """
        try:
            if(self.AccidentsCache.get(state_name) is None):
                #self.AccidentsCache[state_name] = self.search(state_name)
                pass
            else:
                self.AccidentsCache[state_name] += 1
            if(self.AccidentsCache.get(city_name) is None):
                #self.AccidentsCache[city_name] = self.search(city_name)
                pass
            else:
                self.AccidentsCache[city_name] += 1
        except Exception as e:
            logging.error(e)
    def printCache(self):
        """
        Prints out the cache
        """
        try:
            for key, value in self.AccidentsCache.items():
                print(key, ': ', value)
        except Exception as e:
            logging.error(e)

    def clearCache(self):
        """
        Empties the cache
        """
        self.AccidentsCache.clear()