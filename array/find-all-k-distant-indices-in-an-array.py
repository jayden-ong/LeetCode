class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        num_nums = len(nums)
        indices_used = set()
        answer = []
        for i in range(num_nums):
            if nums[i] == key:
                for j in range(max(0, i - k), min(i + k + 1, num_nums)):
                    if j not in indices_used:
                        answer.append(j)
                        indices_used.add(j)
        return answer