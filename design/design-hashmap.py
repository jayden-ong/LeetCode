class MyHashMap:

    def __init__(self):
        self.nums = []
        self.num_nums = 0
        

    def put(self, key: int, value: int) -> None:
        index_to_add = self.num_nums
        for i in range(self.num_nums):
            if key < self.nums[i][0]:
                index_to_add = i
                break
            elif key == self.nums[i][0]:
                self.nums[i][1] = value
                return
        
        self.nums.insert(index_to_add, [key, value])
        self.num_nums += 1
        

    def get(self, key: int) -> int:
        left = 0
        right = self.num_nums - 1
        while left <= right:
            mid = (left + right) // 2
            if key < self.nums[mid][0]:
                right = mid - 1
            elif key == self.nums[mid][0]:
                return self.nums[mid][1]
            else:
                left = mid + 1
        return -1
        
    def remove(self, key: int) -> None:
        left = 0
        right = self.num_nums - 1
        while left <= right:
            mid = (left + right) // 2
            if key < self.nums[mid][0]:
                right = mid - 1
            elif key == self.nums[mid][0]:
                self.nums = self.nums[:mid] + self.nums[mid + 1:]
                self.num_nums -= 1
                return
            else:
                left = mid + 1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)