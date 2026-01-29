class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        # Keep running track of valid amounts
        # We can add, clear, and discard from a SortedList
        #   This list will store (occurrences, num)
        nums_dict = defaultdict(int)
        largest_x = SortedList()
        smallest = SortedList()
        answer = []
        curr_answer = 0
        # Keep track of the valid number that appears the least
        for i in range(len(nums)):  
            # We need to kick out the element outside of the sliding window
            if i >= k:
                # We need to figure out which sorted list it is in
                # It must be in the largest list
                if (nums_dict[nums[i - k]], nums[i - k]) >= largest_x[0]:
                    largest_x.remove((nums_dict[nums[i - k]], nums[i - k]))
                    curr_answer -= nums_dict[nums[i - k]] * nums[i - k]
                else:
                    smallest.remove((nums_dict[nums[i - k]], nums[i - k]))
                
                # We need to add the largest small into the top x
                if smallest and len(largest_x) < x:
                    curr_smallest = smallest[-1]
                    curr_answer += curr_smallest[0] * curr_smallest[1]
                    smallest.remove(curr_smallest)
                    largest_x.add(curr_smallest)
                
                # Update it and reinsert
                nums_dict[nums[i - k]] -= 1
                if len(largest_x) < x or (nums_dict[nums[i - k]], nums[i - k]) > largest_x[0]:
                    largest_x.add((nums_dict[nums[i - k]], nums[i - k]))
                    curr_answer += nums_dict[nums[i - k]] * nums[i - k]
                    # Kick out the worst one if the list is full
                    if len(largest_x) > x:
                        curr_worst = largest_x[0]
                        curr_answer -= curr_worst[0] * curr_worst[1]
                        largest_x.remove(curr_worst)
                        smallest.add(curr_worst)
                else:
                    smallest.add((nums_dict[nums[i - k]], nums[i - k]))

            # It already exists -- we need to clear it and update it
            # If it never existed, there is nothing to remove
            if nums_dict[nums[i]] > 0:
                # We need to figure out which sorted list it is in
                # It must be in the largest list
                if (nums_dict[nums[i]], nums[i]) >= largest_x[0]:
                    largest_x.remove((nums_dict[nums[i]], nums[i]))
                    curr_answer -= nums_dict[nums[i]] * nums[i]
                else:
                    smallest.remove((nums_dict[nums[i]], nums[i]))
                
                # We need to add the largest small into the top x
                if smallest and len(largest_x) < x:
                    curr_smallest = smallest[-1]
                    curr_answer += curr_smallest[0] * curr_smallest[1]
                    smallest.remove(curr_smallest)
                    largest_x.add(curr_smallest)
            
            # We now need to update it and add it to whatever list
            nums_dict[nums[i]] += 1
            # If the "top x" hasn't been decided or it beats the smallest, add it
            if len(largest_x) < x or (nums_dict[nums[i]], nums[i]) > largest_x[0]:
                largest_x.add((nums_dict[nums[i]], nums[i]))
                curr_answer += nums_dict[nums[i]] * nums[i]
                # Kick out the worst one if the list is full
                if len(largest_x) > x:
                    curr_worst = largest_x[0]
                    curr_answer -= curr_worst[0] * curr_worst[1]
                    largest_x.remove(curr_worst)
                    smallest.add(curr_worst)
            else:
                smallest.add((nums_dict[nums[i]], nums[i]))

            if i >= k - 1:
                answer.append(curr_answer)
        return answer