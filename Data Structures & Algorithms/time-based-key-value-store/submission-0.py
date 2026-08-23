class TimeMap:
    def __init__(self):
        # Dictionary to store key: list of [timestamp, value]
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])
        
        # Traditional Binary Search!
        l, r = 0, len(values) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            
            # If our middle timestamp is valid, save the value
            # but keep searching to the right for an even closer one!
            if values[m][0] <= timestamp:
                res = values[m][1]
                l = m + 1
            else:
                r = m - 1
                
        return res