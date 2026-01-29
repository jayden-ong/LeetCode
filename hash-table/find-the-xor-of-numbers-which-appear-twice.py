class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        answer = 0
        nums_set = set()
        for num in nums:
            if num in nums_set:
                answer ^= num
            nums_set.add(num)
        return answer