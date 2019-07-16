import datetime
import uuid
class LRUCache:
    def __init__(self, maxSize):
        self.cacheMaximumSize = maxSize
        #initialize a cache memory store
        self.cacheMemory = {}

    def cache_size(self):
        return len(self.cacheMemory) 

    def update_cache(self, ip):
        #generating time-based random id for entry key
        key = uuid.uuid4()
        if (key not in self.cacheMemory and self.cache_size() >= self.cacheMaximumSize ):
            self.delete_cache_lru()
        new_entry = {"ip": ip, "system_log_time" : datetime.datetime.now()}
        self.cacheMemory[key] = new_entry


    def delete_cache_lru(self):
        previous_key = None
        cacheMem = self.cacheMemory
        for current_key in cacheMem:  
            if( previous_key is not None and cacheMem[current_key]['system_log_time'] < cacheMem[previous_key]['system_log_time'] ):
                previous_key = current_key
            elif previous_key is None:
                #i.e first iteration
                previous_key = current_key

        self.cacheMemory.pop(previous_key)
