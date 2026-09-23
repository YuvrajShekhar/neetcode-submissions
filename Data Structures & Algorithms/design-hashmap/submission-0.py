class MyHashMap:

    def __init__(self):
        self.hashmap = []

    def put(self, key: int, value: int) -> None:
        change = 0
        for item in self.hashmap:
            if item[0]==key:
                self.hashmap.remove(item)
                self.hashmap.append([key,value])
                change +=1

        if change==0:
            self.hashmap.append([key,value])

    def get(self, key: int) -> int:
        for item in self.hashmap:
            if item[0]==key:
                return item[1]

        return -1
        

    def remove(self, key: int) -> None:
        for item in self.hashmap:
            if item[0]==key:
                self.hashmap.remove(item)      


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)