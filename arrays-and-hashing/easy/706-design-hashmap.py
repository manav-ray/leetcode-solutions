class MyHashMap:

    def __init__(self):
        self.size = 10**6 + 1
        self.map = [None] * self.size

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        return self.map[key] if self.map[key] != None else -1

    def remove(self, key: int) -> None:
        self.map[key] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)