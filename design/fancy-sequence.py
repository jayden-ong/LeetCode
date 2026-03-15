class Fancy:

    def __init__(self):
        self.vals = []
        self.length = 0
        self.operations = []

    def append(self, val: int) -> None:
        self.vals.append(val)
        self.length += 1

    def addAll(self, inc: int) -> None:
        self.operations.append((self.length, "add", inc))

    def multAll(self, m: int) -> None:
        self.operations.append((self.length, "multiply", m))
        
    def getIndex(self, idx: int) -> int:
        print(self.vals)
        if idx >= self.length:
            return -1
        
        answer = self.vals[idx]
        ops_reverse = self.operations[::-1]
        for i in range(len(self.operations) - 1, -1, -1):
            last_index, operation, amount = ops_reverse[i]
            if idx >= last_index:
                continue
            
            if operation == "add":
                answer += amount
            else:
                answer *= amount
        return answer


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)