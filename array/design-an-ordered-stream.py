class OrderedStream:

    def __init__(self, n: int):
        self.chunk = [None] * n
        self.n = n
        self.curr_pos = 0
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.chunk[idKey - 1] = value
        answer = []
        for i in range(self.curr_pos, self.n):
            if self.chunk[i] is not None:
                answer.append(self.chunk[i])
            else:
                self.curr_pos = i
                return answer
        self.curr_pos = self.n
        return answer


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)