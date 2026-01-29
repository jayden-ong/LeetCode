class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        
        nums_heap = []
        for num in nums_dict:
            heapq.heappush(nums_heap, (num, nums_dict[num] * num))
        
        prev = None
        prev_prev = None
        dp_dict = {}
        curr_best = 0
        while nums_heap:
            curr_num, curr_score = heapq.heappop(nums_heap)
            if prev is None:
                dp_dict[curr_num] = curr_score
            elif prev_prev is None:
                # Have to make decision - cannot pick both
                if curr_num - 1 == prev:
                    dp_dict[curr_num] = max(curr_score, dp_dict[prev])
                else:
                    dp_dict[curr_num] = curr_score + dp_dict[prev]
            else:
                if curr_num - 1 == prev:
                    dp_dict[curr_num] = max(curr_score + dp_dict[prev_prev], dp_dict[prev])
                else:
                    dp_dict[curr_num] = curr_score + dp_dict[prev]
            
            prev_prev = prev
            prev = curr_num
            curr_best = dp_dict[curr_num]
        return curr_best