class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        first_smallest, second_smallest, first_largest, second_largest = float('inf'), float('inf'), float('-inf'), float('-inf')
        first_smallest_index, second_smallest_index, first_largest_index, second_largest_index = 0, 0, 0, 0
        for i in range(len(arrays)):
            print(arrays[i])
            array_smallest, array_largest = min(arrays[i]), max(arrays[i])
            if array_smallest < first_smallest:
                first_smallest, second_smallest = array_smallest, first_smallest
                first_smallest_index, second_smallest_index = i, first_smallest_index
            elif array_smallest < second_smallest:
                second_smallest = array_smallest
                second_smallest_index = i
            
            if array_largest > first_largest:
                first_largest, second_largest = array_largest, first_largest
                first_largest_index, second_largest_index = i, first_largest_index
            elif array_largest > second_largest:
                second_largest = array_largest
                second_largest_index = i
        
        if first_smallest_index != first_largest_index:
            return abs(first_largest - first_smallest)

        candidates = []
        if first_largest_index != second_smallest_index:
            candidates.append(abs(first_largest - second_smallest))
        if second_largest_index != first_smallest_index:
            candidates.append(abs(second_largest - first_smallest))
        return max(candidates)