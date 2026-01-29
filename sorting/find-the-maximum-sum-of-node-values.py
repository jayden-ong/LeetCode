class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        num_change = 0
        curr_sum = 0
        # Represents the value is counterpart is the smallest
        # It means swapping causes the least damage
        smallest_diff = (float('inf'), None, None)
        # Second element is original value and third element is new value
        for num in nums:
            if num ^ k > num:
                num_change += 1
                curr_sum += num ^ k
                if (num ^ k) - num < smallest_diff[0]:
                    smallest_diff = ((num ^ k) - num, num ^ k, num)
            else:
                curr_sum += num
                if num - (num ^ k) < smallest_diff[0]:
                    smallest_diff = (num - (num ^ k), num, num ^ k)
        
        if num_change % 2 == 0:
            return curr_sum
        return curr_sum - smallest_diff[0]
        # Need to get smallest difference between a num and its counterpart