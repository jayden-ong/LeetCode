class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # We only need the min and max to verify a valid subarray
        min_heap = []
        max_heap = []
        left = 0
        right = 0
        answer = 0
        while right < len(nums):
            heapq.heappush(max_heap, (-nums[right], right))
            heapq.heappush(min_heap, (nums[right], right))

            # Want to keep removing the current min or max if difference is greater than limit
            while -max_heap[0][0] - min_heap[0][0] > limit:
                # Want to remove the soonest item
                left = min(max_heap[0][1], min_heap[0][1])
                
                # Want to remove all items in max and min heaps that are earlier than left
                # Only care about items smaller/larger than curr
                while max_heap[0][1] <= left:
                    heapq.heappop(max_heap)
                
                while min_heap[0][1] <= left:
                    heapq.heappop(min_heap)

                left += 1
                
            answer = max(answer, right - left + 1)
            right += 1
        return answer