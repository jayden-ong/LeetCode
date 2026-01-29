class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        k_set = set()
        num_opers = 0
        for i in range(len(nums) - 1, -1, -1):
            num_opers += 1
            if nums[i] <= k and nums[i] not in k_set:
                k_set.add(nums[i])
                if len(k_set) == k:
                    return num_opers
        return num_opers