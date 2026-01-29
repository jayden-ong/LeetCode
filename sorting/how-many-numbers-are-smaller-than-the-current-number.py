class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_copy = nums.copy()
        nums_copy.sort()
        rank_dict = {}
        curr_rank = 0
        for num in nums_copy:
            if num not in rank_dict:
                rank_dict[num] = curr_rank
            curr_rank += 1
        
        answer = []
        for num in nums:
            answer.append(rank_dict[num])
        
        return answer