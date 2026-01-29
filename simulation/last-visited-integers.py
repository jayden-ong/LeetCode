class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen = []
        ans = []
        consecutive_negative = 0
        for num in nums:
            if num != -1:
                seen = [num] + seen
                consecutive_negative = 0
            else:
                consecutive_negative += 1
                if consecutive_negative <= len(seen):
                    ans.append(seen[consecutive_negative - 1])
                else:
                    ans.append(-1)
        return ans