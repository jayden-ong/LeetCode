class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_cand = 1
        curr_cand = nums[0]

        for i in range(1, len(nums)):
            if curr_cand != nums[i] and num_cand <= 0:
                num_cand = 1
                curr_cand = nums[i]
            elif curr_cand != nums[i]:
                num_cand -= 1
            else:
                num_cand += 1
        
        return curr_cand