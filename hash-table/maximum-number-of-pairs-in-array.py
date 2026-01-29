class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        
        num_pairs = 0
        leftover = 0
        for num in nums_dict:
            num_pairs += nums_dict[num] // 2
            leftover += nums_dict[num] % 2
        return [num_pairs, leftover] 