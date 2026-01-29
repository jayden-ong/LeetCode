class Solution:
    def countElements(self, nums: List[int]) -> int:
        smallest = float('inf')
        num_smallest = 0
        largest = float('-inf')
        num_largest = 0
        num_nums = 0
        for num in nums:
            if num < smallest:
                smallest = num
                num_smallest = 1
            elif num == smallest:
                num_smallest += 1

            if num > largest:
                largest = num
                num_largest = 1
            elif num == largest:
                num_largest += 1

            num_nums += 1
        return max(num_nums - num_largest - num_smallest, 0)