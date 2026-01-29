class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        num_nums = len(nums)
        answer = -1
        smallest = float('inf')
        largest = float('-inf')
        for i in range(1, num_nums):
            if nums[i - 1] < nums[i]:
                if nums[i - 1] < smallest:
                    smallest = nums[i - 1]
                    largest = nums[i]
                else:
                    smallest = min(smallest, nums[i - 1])
                    largest = max(largest, nums[i])
                
                answer = max(answer, largest - smallest)
                
        return answer