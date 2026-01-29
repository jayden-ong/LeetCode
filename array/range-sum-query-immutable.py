class NumArray:

    def __init__(self, nums: List[int]):
        self.sum_before = []
        curr = 0
        for num in nums:
            curr += num
            self.sum_before.append(curr)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sum_before[right]
        return self.sum_before[right] - self.sum_before[left - 1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)