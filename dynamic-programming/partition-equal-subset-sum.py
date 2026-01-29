class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 != 0:
            return False
        required_sum = sum_nums // 2
        
        # Want a dictionary to store what sums we can and cannot make at certain indicices
        memo_dict = {}

        def choice(curr_index, curr_sum):
            if curr_index in memo_dict and curr_sum in memo_dict[curr_index]:
                return False
            
            if curr_sum == required_sum:
                return True
            
            if curr_index >= len(nums) or curr_sum > required_sum:
                return False
            
            if curr_sum + nums[curr_index] == required_sum:
                return True
            
            result = choice(curr_index + 1, curr_sum + nums[curr_index]) or choice(curr_index + 1, curr_sum)
            if curr_index not in memo_dict:
                memo_dict[curr_index] = set()
            
            if not result:
                memo_dict[curr_index].add(curr_sum)
            return result

        return choice(0, 0)