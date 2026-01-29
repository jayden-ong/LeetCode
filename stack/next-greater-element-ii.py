class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # The only entries that will have -1 are the ones that have max
        highest = max(nums)
        answer = [0] * len(nums)
        i = 0
        while i < len(nums):
            # Want to find the next maximum
            if nums[i] == highest:
                answer[i] = -1
                i += 1
            else:
                if i == 0 or (nums[i] >= answer[i - 1]) or (nums[i - 1] > nums[i]):
                    j = i + 1
                    j %= len(nums)
                    while j != i and nums[j] <= nums[i]:
                        j += 1
                        j %= len(nums)
                    answer[i] = nums[j]
                elif nums[i - 1] <= nums[i] < answer[i - 1]:
                    # Need to look at previous entry
                    # If the current entry is smaller than last entry, must be the same
                    answer[i] = answer[i - 1]
                    
                i += 1
        return answer