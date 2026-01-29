class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        nums_seen = set()
        answer = 0
        next_available = 0
        i = 0
        for num in nums:
            if num in nums_seen:
                # For an input, if we increment the current num by 1, 
                # we are guaranteed a unique number(so far) since all numbers
                # are less than or equal to the current number
                answer += next_available - num
                nums_seen.add(next_available)
                next_available += 1
            else:
                nums_seen.add(num)
                next_available = num + 1
            i += 1
        return answer