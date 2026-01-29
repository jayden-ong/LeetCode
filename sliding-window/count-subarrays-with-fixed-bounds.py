class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        answer = 0
        left = 0
        min_queue = deque()
        max_queue = deque()
        for i, num in enumerate(nums):
            if minK <= num <= maxK:
                while min_queue and num <= nums[min_queue[-1]]:
                    min_queue.pop()
                min_queue.append(i)

                while max_queue and num >= nums[max_queue[-1]]:
                    max_queue.pop()
                max_queue.append(i)
                if nums[min_queue[0]] == minK and nums[max_queue[0]] == maxK:
                    answer += (min(min_queue[0], max_queue[0]) - left + 1)
            else:
                min_queue = deque()
                max_queue = deque()
                left = i + 1
        return answer