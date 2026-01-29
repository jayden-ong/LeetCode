class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        nums_indices = [0] * len(nums)
        nums_heap = []
        num_numbers = 0
        lowest = float('inf')
        highest = float('-inf')
        # Will use later
        greatest_number = float('-inf')
        for i in range(len(nums)):
            nums_list = nums[i]
            lowest = min(lowest, nums_list[0])
            highest = max(highest, nums_list[0])
            heapq.heappush(nums_heap, (nums_list[0], i))
            num_numbers += len(nums_list)
            greatest_number = max(greatest_number, nums_list[-1])
        
        answer = [lowest, highest] 
        curr_highest = highest
        for i in range(num_numbers):
            prev_lowest, index_of_lowest = heapq.heappop(nums_heap)
            nums_indices[index_of_lowest] += 1
            if nums_indices[index_of_lowest] < len(nums[index_of_lowest]):
                heapq.heappush(nums_heap, (nums[index_of_lowest][nums_indices[index_of_lowest]], index_of_lowest))
                curr_lowest = nums_heap[0][0]
                curr_highest = max(curr_highest, nums[index_of_lowest][nums_indices[index_of_lowest]])
            else:
                # One list has exhausted all of its numbers. All other solutions have to be larger.
                return answer
            
            if curr_highest - curr_lowest < answer[1] - answer[0]:
                answer = [curr_lowest, curr_highest]

        return answer

            

        
            
