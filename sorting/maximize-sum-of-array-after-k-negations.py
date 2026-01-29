class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        num_nums = len(nums)
        for i in range(num_nums):
            if k == 0:
                return sum(nums)
            else:
                if nums[i] < 0:
                    nums[i] = nums[i] * -1
                    k -= 1
                elif nums[i] == 0:
                    return sum(nums)
                else:
                    if k % 2 == 0:
                        return sum(nums)
                    else:
                        if i > 0 and abs(nums[i - 1]) < abs(nums[i]):
                            nums[i - 1] = nums[i - 1] * -1
                        else:
                            nums[i] = nums[i] * -1
                        return sum(nums)    
        if k > 0 and k % 2 == 1:
            return sum(nums) - (2 * nums[-1])
        return sum(nums)