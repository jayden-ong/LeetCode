class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        answer = []
        suffix_dict = {}
        length_suffix = 0
        for num in nums:
            if num in suffix_dict:
                suffix_dict[num] += 1
            else:
                suffix_dict[num] = 1
                length_suffix += 1
        
        num_nums = len(nums)
        prefix_set = set()
        length_prefix = 0
        for i in range(num_nums):
            suffix_dict[nums[i]] -= 1
            if suffix_dict[nums[i]] <= 0:
                length_suffix -= 1
            
            if nums[i] not in prefix_set:
                prefix_set.add(nums[i])
                length_prefix += 1
            answer.append(length_prefix - length_suffix)
        return answer