class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table = {}

    def getLoadFactor(self) -> float:
        return ((len(self.table.keys())) / self.capacity)

    def insert(self, key: int, value: int) -> None:
        self.table[key] = value
        load_factor = self.getLoadFactor()
        if load_factor >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        if key not in self.table.keys():
            return -1
        else:
            return self.table[key]

    def remove(self, key: int) -> bool:
        if key not in self.table.keys():
            return False
        else:
            del self.table[key]
            return True

    def getSize(self) -> int:
        return len(self.table.keys())

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity = self.capacity * 2