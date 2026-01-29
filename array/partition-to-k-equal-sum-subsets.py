class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # The subsets have to have sum // k
        nums_sum = sum(nums)
        required = nums_sum // k
        if nums_sum % k != 0:
            return False
        
        # We need k subsets that add up to required
        subsets = [0] * k
        # If we fail, want to fail early
        nums.sort(reverse=True)

        def recursive(curr_index):
            if curr_index == len(nums):
                return True
            
            # Try adding nums[curr_index] to each subset
            for i in range(len(subsets)):
                if subsets[i] + nums[curr_index] <= required:
                    subsets[i] += nums[curr_index]
                    # Try finding a solution now that nums[curr_index] is used
                    if recursive(curr_index + 1):
                        return True
                    
                    subsets[i] -= nums[curr_index]

                    # Initially, all of our subsets are 0
                    # If our current subset is 0, means we failed and don't have to try anything else
                    # because all future subsets are also 0
                    if subsets[i] == 0:
                        break
            return False
        
        return recursive(0)