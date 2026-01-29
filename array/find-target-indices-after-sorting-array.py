class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        answer = []
        i = 0
        for num in nums:
            if num == target:
                answer.append(i)
            i += 1
        return answer