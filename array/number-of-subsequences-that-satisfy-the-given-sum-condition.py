class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        right = len(nums) - 1
        nums_valid_index = []
        MOD = 10 ** 9 + 7
        # Want to figure out what index makes min + max > target
        # If they are equal, means invalid
        for i in range(len(nums)):
            while right > i and nums[i] + nums[right] > target:
                right -= 1
            right = max(right, i)
            nums_valid_index.append(right + 1)
        
        # Number of subsequences is n * (n + 1) / 2
        answer = 0
        for i in range(len(nums_valid_index)):
            changeable_length = nums_valid_index[i] - i - 1
            if changeable_length == 0 and nums[i] * 2 > target:
                continue
                
            answer += 2 ** changeable_length
            answer %= MOD
        return answer