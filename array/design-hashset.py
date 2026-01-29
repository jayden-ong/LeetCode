class MyHashSet:

    def __init__(self):
        self.nums = []
        self.num_nums = 0
        

    def add(self, key: int) -> None:
        index_to_add = self.num_nums
        for i in range(self.num_nums):
            if key < self.nums[i]:
                index_to_add = i
                break
            elif key == self.nums[i]:
                return
        
        self.nums.insert(index_to_add, key)
        self.num_nums += 1

    def remove(self, key: int) -> None:
        left = 0
        right = self.num_nums - 1
        while left <= right:
            mid = (left + right) // 2
            if key < self.nums[mid]:
                right = mid - 1
            elif key == self.nums[mid]:
                self.nums = self.nums[:mid] + self.nums[mid + 1:]
                self.num_nums -= 1
                return
            else:
                left = mid + 1

    def contains(self, key: int) -> bool:
        #print(self.nums)
        left = 0
        right = self.num_nums - 1
        while left <= right:
            mid = (left + right) // 2
            if key < self.nums[mid]:
                right = mid - 1
            elif key == self.nums[mid]:
                return True
            else:
                left = mid + 1
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)