from Cache import LRUCache
import random

if __name__ == "__main__":
    cacheMemoryMaxSize = 15 #we want the maximum size of the Cache to be 15
    myCache = LRUCache(cacheMemoryMaxSize)
    key_range = list(range(1,51)) #we want 50 iterations
    network_ips = ["192.168.0.1", "192.168.0.34", "192.168.0.45", "192.168.20.1", "192.168.20.29",
                   "192.168.35.12", "192.168.35.40", "192.168.35.75", "192.168.35.135", "192.168.35.240"] #dummy network addresses
    for key in key_range:    
        #secure    
        secure_random = random.SystemRandom()
        ip = secure_random.choice(network_ips)
        print(" iteration  ", key, "selecting ip ", ip)
        myCache.update_cache(ip)
    
    for cache_values in myCache.cacheMemory:
        print("Cached IP: ", myCache.cacheMemory[cache_values])

    