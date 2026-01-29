class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # [5, 2, 4, 0, 1]
        # [(5), (1, 2), (0, 1, 2), (4, 5, 0), (5, 0, 1)]
        if len(nums) <= 1:
            return False

        # sums[i] will store the sum for nums[i + 1:]
        '''
        sums = [0]
        curr = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            sums.append(curr)
            curr += nums[i]
        sums = sums[::-1]
        '''
        # Get the prefix mod and if it already exists, then we must have added a multiple of k
        # If the difference between indices is greater than 1, the subset sum is between
        dp_dict = {}
        # dp_dict[0] = -1 means we start with a mod of 0
        dp_dict[0] = -1
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum = (curr_sum + nums[i]) % k
            if curr_sum in dp_dict and i - dp_dict[curr_sum] > 1:
                return True
            
            if curr_sum not in dp_dict:
                dp_dict[curr_sum] = i
        return False