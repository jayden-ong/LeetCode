class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        curr = 0
        answer = 0
        answer_dict = {}
        answer_dict[0] = -1
        i = 0
        for num in nums:
            if num == 0:
                curr -= 1
            else:
                curr += 1
            
            if curr not in answer_dict:
                answer_dict[curr] = i
            
            if curr in answer_dict:
                answer = max(answer, i - answer_dict[curr])
            i += 1
        return answer