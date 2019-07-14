from Cache import Cache
import random

if __name__ == "__main__":
    myCache = Cache()
    key_range = list(range(1,9))
    network_ips = ["192.168.0.1", "192.168.0.34", "192.168.0.45", "192.168.20.1", "192.168.20.29",
                   "192.168.35.12", "192.168.35.40", "192.168.35.75", "192.168.35.135", "192.168.35.240",
                    "192.168.60.2", "192.168.60.10", "192.168.65.30", "192.168.65.40", "192.168.65.70", "192.168.65.125"]
    
    for key in key_range:       
        secure_random = random.SystemRandom()
        item = secure_random.choice(network_ips)
        print(" iterating through entry index ", key, "ip ", item)
        myCache.update_cache(key, item)
    
    for cache_values in myCache.cacheMemory:
        print("Cached IP: ", myCache.cacheMemory[cache_values])

    