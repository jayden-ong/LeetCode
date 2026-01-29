class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev_one_index = None
        num_nums = len(nums)
        for i in range(num_nums):
            if nums[i] == 1:
                if prev_one_index is None:
                    prev_one_index = i
                else:
                    if i - prev_one_index - 1 < k:
                        return False
                    prev_one_index = i
        return True
