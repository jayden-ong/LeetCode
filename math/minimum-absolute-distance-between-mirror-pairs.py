class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        nums_dict = {}
        answer = float('inf')
        for i, num in enumerate(nums):
            if num in nums_dict:
                answer = min(answer,  i - nums_dict[num])
            nums_dict[int(str(num)[::-1])] = i

        if answer == float('inf'):
            return -1
        return answer