class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(nums):
            if len(nums) <= 1:
                return nums
            
            mid = len(nums) // 2
            left = mergesort(nums[:mid])
            right = mergesort(nums[mid:])

            left_index = 0 
            right_index = 0
            answer = []
            while left_index < len(left) and right_index < len(right):
                if left[left_index] < right[right_index]:
                    answer.append(left[left_index])
                    left_index += 1
                else:
                    answer.append(right[right_index])
                    right_index += 1
            
            if left_index < len(left):
                return answer + left[left_index:]
            return answer + right[right_index:]
        return mergesort(nums)