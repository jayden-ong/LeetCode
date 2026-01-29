class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # Want to keep erasing until you see a duplicate elemenet
        sum_nums = []
        curr_sum = 0
        erased_elements = {}
        answer = float('-inf')
        sum_since_erase = 0
        last_erase_index = float('-inf')
        for i, num in enumerate(nums):
            answer = max(answer, sum_since_erase)
            curr_sum += num
            sum_nums.append(curr_sum)
            sum_since_erase += num

            if num in erased_elements and erased_elements[num] > last_erase_index:
                sum_since_erase = curr_sum - sum_nums[erased_elements[num]]
                answer = max(sum_since_erase, answer)
                last_erase_index = erased_elements[num]

                
            elif i == len(nums) - 1:
                answer = max(answer, sum_since_erase)
            
            erased_elements[num] = i
        return answer