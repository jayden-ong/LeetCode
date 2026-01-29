class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        # Want to remove the largest numbers from the first sum
        # Want to remove the lowest numbers from the second sum
        elements_to_remove = len(nums) // 3
        # Find the min sum of elements less than or equal to i
        min_sums = []
        largest_nums = []
        curr_sum = 0
        for i in range(len(nums)):
            heapq.heappush(largest_nums, -nums[i])
            curr_sum += nums[i]
            if len(largest_nums) < elements_to_remove:
                min_sums.append(None)
            elif len(largest_nums) == elements_to_remove:
                min_sums.append(curr_sum)
            else:
                curr_sum += heapq.heappop(largest_nums)
                min_sums.append(curr_sum)
        
        max_sums = []
        smallest_nums = []
        curr_sum = 0
        for i in range(len(nums) - 1, -1, -1):
            heapq.heappush(smallest_nums, nums[i])
            curr_sum += nums[i]
            if len(smallest_nums) < elements_to_remove:
                max_sums.append(None)
            elif len(smallest_nums) == elements_to_remove:
                max_sums.append(curr_sum)
            else:
                curr_sum -= heapq.heappop(smallest_nums)
                max_sums.append(curr_sum)
        max_sums = max_sums[::-1]
        
        answer = float('inf')
        for i in range(1, len(max_sums)):
            if min_sums[i - 1] is not None and max_sums[i] is not None:
                answer = min(answer, min_sums[i - 1] - max_sums[i])
        return answer