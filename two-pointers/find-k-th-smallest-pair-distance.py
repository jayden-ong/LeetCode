class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        '''
        distance_heap = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                heapq.heappush(distance_heap, abs(nums[i] - nums[j]))
        
        num_searched = 0
        while distance_heap:
            num_searched += 1
            curr = heapq.heappop(distance_heap)
            if num_searched == k:
                return curr
        # Should never run
        return -1
        '''

        # Want to binary search
        # We start with 0 and the max - min
        # We then count the number of pairs with a distance smaller than that
        # If the number of pairs is smaller, it means our distance is too constrictive
        # If it is higher, it means our distance is too generous
        nums.sort()

        def count_pairs_smaller(max_dist):
            answer = 0
            curr = 0
            for j in range(len(nums)):
                # We don't have to check all
                # If the current distance is too big, we need to increase the left pointer
                # If it is less, then all indices in between are also valid
                while nums[j] - nums[curr] > max_dist:
                    curr += 1
                answer += j - curr
            return answer

        lower = 0
        higher = nums[-1] - nums[0]
        while lower < higher:
            mid = (lower + higher) // 2
            
            # Count number of pairs with smaller distance
            if count_pairs_smaller(mid) < k:
                lower = mid + 1
            else:
                higher = mid

        return lower
    