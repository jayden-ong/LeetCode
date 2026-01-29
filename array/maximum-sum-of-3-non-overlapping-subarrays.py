class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        first_sum = 0
        for i in range(k):
            first_sum += nums[i]
        second_sum = 0
        for i in range(k, 2 * k):
            second_sum += nums[i]
        third_sum = 0
        for i in range(2 * k, 3 * k):
            third_sum += nums[i]
        
        max_first_sum = first_sum
        max_second_sum = first_sum + second_sum
        max_third_sum = first_sum + second_sum + third_sum

        answer = [0, k, 2 * k]
        curr_first_second_index, curr_first_index, curr_second_index, curr_third_index = 0, 0, k, 2 * k
        for i in range(1, len(nums) - (3 * k) + 1):
            # Remove last element and add next element
            first_sum -= nums[i - 1]
            first_sum += nums[i + k - 1]
            second_sum -= nums[i + k - 1]
            second_sum += nums[i + (2 * k) - 1]
            third_sum -= nums[i + (2 * k) - 1]
            third_sum += nums[i + (3 * k) - 1]

            # Need to get highest first_sum
            if first_sum > max_first_sum:
                max_first_sum = first_sum
                curr_first_index = i
            
            # Need to get highest second_sum
            # If we don't update curr_first_index, it will get stuck at the absolute maximum
            if max_first_sum + second_sum > max_second_sum:
                max_second_sum = max_first_sum + second_sum
                curr_first_second_index = curr_first_index
                curr_second_index = i + k
            
            if max_second_sum + third_sum > max_third_sum:
                max_third_sum = max_second_sum + third_sum
                answer = [curr_first_second_index, curr_second_index, i + 2 * k]
        
        return answer