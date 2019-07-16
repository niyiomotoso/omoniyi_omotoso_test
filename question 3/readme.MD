Language: Python

Program: Cache LRU Library, A Geo Distributed LRU (Least Recently Used) cache with time expiration.

Implementation

- The program was implemented in CacheMain for a Cache with Max Size of 15 but can be changed depending on use case.


- The algorithm used for the Cache dynamcis is time-based First In First Out (FIFO).


-  A time-based random unique id is generated and used as the key for each cached IP Address.


- A date time is attached to each cached IP address as well.


- IP addresses are popped from the Cache list once the set limit is reached.



Usage

- Import LRUCache from class Cache

- Create an instance of LRUCache and supply it with the maximum cache size as expected in its constructor.

- Call the the function update_cache for every IP that needs to be cached. The library handles the rest.

- A full example is found in CacheMain.


Missing Functionality

The library doesn't yet handle Geo Distribution.






