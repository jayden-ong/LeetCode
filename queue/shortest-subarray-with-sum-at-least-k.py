class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # Combine sequences of positive and negative numbers into groups
        '''
        curr = 0
        positive = True
        sections = []
        for num in nums:
            if num < 0 and positive:
                positive = False
                sections.append(curr)
                curr = num
            elif num > 0 and not positive:
                positive = True
                sections.append(curr)
                curr = num
            else:
                curr += num
        if curr != 0:
            sections.append(curr)
        
        # Check if solution is possible
        best = 0
        possible_solution = False
        for section in sections:
            best += section
            if best >= k:
                possible_solution = True
                break
            
            if best < 0:
                best = 0
        if not possible_solution:
            return -1
        
        answer = float('inf')
        for i in range(len(nums)):
            if nums[i] > 0:
                if answer == float('inf'):
                    end = len(nums)
                else:
                    end = min(len(nums), i + answer)
                curr = 0
                for j in range(i, end):
                    curr += nums[j]
                    if curr <= 0:
                        break
                    elif curr >= k:
                        answer = min(answer, j - i + 1)
        if answer == float('inf'):
            return -1
        return answer
        '''

        prefix_sum_heap = []
        curr = 0
        answer = float('inf')
        for i in range(len(nums)):
            curr_num = nums[i]
            curr += curr_num
            # Catches all subarrays that start at index 0
            if curr >= k:
                answer = min(answer, i + 1)
            
            # Catches all subarrays that don't start at index 0 
            # This condition checks if the heap is not empty and curr - prefix_sum_heap[0][0] is the
            # sum from index prefix_sum_heap[0][1] to i
            while prefix_sum_heap and curr - prefix_sum_heap[0][0] >= k:
                answer = min(answer, i - heapq.heappop(prefix_sum_heap)[1])
            heapq.heappush(prefix_sum_heap, (curr, i))

        if answer == float('inf'):
            return -1
        return answer