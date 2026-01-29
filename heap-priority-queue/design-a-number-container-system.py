class NumberContainers:

    def __init__(self):
        self.nums_dict = {}
        self.nums_to_indices = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.nums_dict[index] = number
        heapq.heappush(self.nums_to_indices[number], index)

    def find(self, number: int) -> int:
        while self.nums_to_indices[number]:
            if self.nums_dict[self.nums_to_indices[number][0]] == number:
                return self.nums_to_indices[number][0]
            heapq.heappop(self.nums_to_indices[number])
        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)