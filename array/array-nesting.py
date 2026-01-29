class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        answer = 0
        nums_explored = set()
        for i in range(len(nums)):
            if i not in nums_explored:
                streak = 0
                numbers_seen = set()
                curr = nums[i]
                while curr not in numbers_seen:
                    numbers_seen.add(curr)
                    nums_explored.add(curr)
                    curr = nums[curr]
                    streak += 1
                answer = max(answer, streak)
        return answer