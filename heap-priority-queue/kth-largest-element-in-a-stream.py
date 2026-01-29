class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort()
        num_nums = len(nums)
        # Only need to keep track of the first k numbers
        if num_nums < k:
            self.nums = nums
        else:
            self.nums = nums[num_nums - k:]
        # Keep track of k for second function
        self.k = k
        # Keep track of length of list
        self.num_nums = num_nums

    def add(self, val: int) -> int:
        if self.num_nums < self.k:
            #print(self.nums)
            index_to_add = self.num_nums
            for i in range(self.num_nums):
                if val < self.nums[i]:
                    index_to_add = i
                    break

            self.nums.insert(index_to_add, val)
            self.num_nums += 1
            #print(self.nums)
            return self.nums[0]
        # If val added is smaller than KthLargest, nothing changes
        if val <= self.nums[0]:
            return self.nums[0]
        # If val added is smaller than KthLargest, go one back
        index_to_add = self.k
        for i in range(self.k):
            if val < self.nums[i]:
                index_to_add = i
                break

        self.nums.insert(index_to_add, val)
        self.nums = self.nums[1:]
        return self.nums[0]

                


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)