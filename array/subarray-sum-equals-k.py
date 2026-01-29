class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sub_dict = {}
        sub_dict[0] = 1
        curr = 0
        answer = 0
        for num in nums:
            curr += num
            if curr - k in sub_dict:
                answer += sub_dict[curr - k]
            
            if curr in sub_dict:
                sub_dict[curr] += 1
            else:
                sub_dict[curr] = 1
        return answer