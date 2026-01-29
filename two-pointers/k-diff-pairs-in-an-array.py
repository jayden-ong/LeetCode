class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        
        answer = 0
        for num in nums_dict:
            nums_dict[num] -= 1
            if num - k in nums_dict and nums_dict[num - k] > 0:
                answer += 1
            nums_dict[num] += 1
        return answer