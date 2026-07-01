class TimeMap:

    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key  in self.dict.keys():
            self.dict[key].append([timestamp,value])
        else:
            self.dict[key]=[[timestamp,value]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""
        search_space = self.dict[key]
        low = 0
        high = len(search_space)-1
        result = -1
        while low<=high:
            mid = (low+high)//2
            if search_space[mid][0]<=timestamp:
                result = max(mid,result)
                low = mid+1
            elif search_space[mid][0]>timestamp:
                high = mid-1
            
        return search_space[result][1] if result!=-1 else ""


        
