class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            solved = False
            for i in range(num):
                if i | (i + 1) == num:
                    answer.append(i)
                    solved = True
                    break
            if not solved:
                answer.append(-1)
            
        return answer