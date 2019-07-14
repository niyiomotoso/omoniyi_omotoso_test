import datetime

class Cache:
    def __init__(self):
        self.cacheMaximumSize = 4
        self.cacheMemory = {}

    
    def update_cache(self, key, ip):
        if (key not in self.cacheMemory and len(self.cacheMemory) >= self.cacheMaximumSize ):
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
