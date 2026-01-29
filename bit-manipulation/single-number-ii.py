class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one, two = 0, 0
        for num in nums:
            two = two ^ (one & num)
            one = one ^ num
            three = (one & two)

            one = ~three & one
            two = ~three & two
        return one