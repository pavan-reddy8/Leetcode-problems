class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key]=[(value,timestamp)]
        else:
            self.d[key].append((value,timestamp))
        
        
    def get(self, key: str, timestamp: int) -> str:
            values = self.d.get(key,[])
            l =0
            r = len(values) -1
            res = ""
            
            while l<=r :
                mid = (l+r)//2
                if values[mid][1] == timestamp:
                    res = values[mid][0]
                    break
                elif values[mid][1] > timestamp:
                    r = mid-1
                else:
                    res = values[mid][0]
                    l = mid+1
            return res
                    
                


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)