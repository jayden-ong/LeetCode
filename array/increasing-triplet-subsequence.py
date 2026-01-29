class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return False
        # Store a list where each index represents max from index on
        maxes = [nums[-1]]
        curr_max = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            curr_max = max(curr_max, nums[i])
            maxes.append(curr_max)
        maxes = maxes[::-1]
    
        # Store a list where each index represents min up to index
        mins = [nums[0]]
        curr_min = nums[0]
        for i in range(1, len(nums)):
            curr_min = min(curr_min, nums[i])
            mins.append(curr_min)
        
        for i in range(1, len(nums) - 1):
            if mins[i - 1] < nums[i] < maxes[i + 1]:
                return True
        return False
        
        '''
        # Brute force?
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                if nums[i] < nums[j]:
                    if nums[j] < maxes[j + 1]:
                        return True
        return False
        '''
        '''
        # dp? store the longest increasing subsequence?
        if len(nums) <= 2:
            return False
        
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    if dp[i] >= 3:
                        return True
        return False
        '''