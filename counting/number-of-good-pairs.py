class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums_dict = {}
        answer = 0
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 1
            else:
                answer += nums_dict[num]
                nums_dict[num] += 1
        return answer
