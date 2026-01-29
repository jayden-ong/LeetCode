class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        index_to_val = {}
        sums_queue = []
        index_to_remove = set()
        index_to_neighbors = {}
        for i in range(len(nums) - 1):
            index_to_val[i] = nums[i]
            curr = []
            if i > 0:
                curr.append(i - 1)
            else:
                curr.append(float('-inf'))
            
            if i < len(nums) - 1:
                curr.append(i + 1)
            else:
                curr.append(float('-inf'))
            
            index_to_neighbors[i] = curr

            heapq.heappush(sums_queue, (nums[i] + nums[i + 1], i))
            if nums[i] > nums[i + 1]:
                index_to_remove.add(i)
        index_to_val[len(nums) - 1] = nums[-1]
        
        answer = 0
        while index_to_remove:
            # print(index_to_val)
            # print(sums_queue)
            # print(index_to_remove)
            # print(index_to_neighbors)
            # print("\n")
            while True:
                # To account for changing vals 
                # assume sums_queue is not empty 
                index_less, index_more = index_to_neighbors[sums_queue[0][1]]
                if index_to_val[sums_queue[0][1]] == float('-inf') or index_more == float('-inf'):
                    _, _ = heapq.heappop(sums_queue)
                    continue
                
                curr = index_to_val[sums_queue[0][1]] + index_to_val[index_more]
                new_val, remove = heapq.heappop(sums_queue)
                if curr == new_val:
                    break
            
            # "remove" is the index we alter in index_to_val
            index_to_val[remove] = new_val
            old_index_more = index_to_neighbors[remove][1]
            index_to_val[old_index_more] = float('-inf')
            answer += 1
            # Its neighbor ahead changes since that val is gone
            # If it is the last possible index, its new neighbor is float('-inf')
            # print(remove)
            curr_index = len(nums)
            if old_index_more < len(nums) - 1:
                curr_index = index_to_neighbors[old_index_more][1]
            '''
            while curr_index < len(nums) and index_to_val[curr_index] == float('-inf'):
                print("hi")
                curr_index += 1
            '''
            
            if curr_index != float('-inf') and curr_index < len(nums):
                index_to_neighbors[remove][1] = curr_index 
                if curr_index < len(nums) - 1:
                    index_to_neighbors[curr_index][0] = remove
                heapq.heappush(sums_queue, (index_to_val[remove] + index_to_val[curr_index], remove))
            else:
                index_to_neighbors[remove][1] = float('-inf')
            # Now update the problems set
            # First, remove "remove + 1" since it no longer exists
            if old_index_more in index_to_remove:
                index_to_remove.remove(old_index_more)
            
            # Still bad
            if index_to_neighbors[remove][1] != float('-inf'):
                if index_to_val[remove] > index_to_val[index_to_neighbors[remove][1]]:
                    index_to_remove.add(remove)
                elif remove in index_to_remove:
                    index_to_remove.remove(remove)
            elif remove in index_to_remove:
                index_to_remove.remove(remove)
            
            # Have to update previous
            prev = index_to_neighbors[remove][0]
            if prev != float('-inf'):
                heapq.heappush(sums_queue, (index_to_val[prev] + index_to_val[remove], prev))
                if index_to_val[prev] > index_to_val[remove]:
                    index_to_remove.add(prev)
                elif prev in index_to_remove:
                    index_to_remove.remove(prev)
            else:
                if prev in index_to_remove:
                    index_to_remove.remove(prev)
        
        return answer