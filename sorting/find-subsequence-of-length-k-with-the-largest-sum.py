class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        original_nums = nums.copy()
        nums.sort()
        desired_dict = {}
        desired = nums[-k:]
        for num in desired:
            if num in desired_dict:
                desired_dict[num] += 1
            else:
                desired_dict[num] = 1
        
        answer = []
        for num in original_nums:
            if num in desired_dict and desired_dict[num] > 0:
                answer.append(num)
                desired_dict[num] -= 1
        return answer