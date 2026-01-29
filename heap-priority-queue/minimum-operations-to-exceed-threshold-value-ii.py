class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # If there is only one element left, stop?
        heapq.heapify(nums)
        answer = 0
        while len(nums) > 1 and nums[0] < k:
            smallest = heapq.heappop(nums)
            next_smallest = heapq.heappop(nums)
            heapq.heappush(nums, min(smallest, next_smallest) * 2 + max(smallest, next_smallest))
            answer += 1
        return answer
