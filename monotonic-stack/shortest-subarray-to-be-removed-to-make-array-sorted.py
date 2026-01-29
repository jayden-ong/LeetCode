class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        arr_reversed = arr[::-1]
        no_changes = True
        for i in range(len(arr) - 1):
            if arr[i + 1] < arr[i]:
                no_changes = False
                break
        
        if no_changes:
            return 0
        
        longest_sorted_left = 1
        stop_left = False
        longest_sorted_right = 1
        stop_right = False
        for i in range(len(arr) - 1):
            if arr[i + 1] >= arr[i] and not stop_left:
                longest_sorted_left += 1
            else:
                stop_left = True
            
            if arr_reversed[i + 1] <= arr_reversed[i] and not stop_right:
                longest_sorted_right += 1
            else:
                stop_right = True
        
        answer = max(longest_sorted_left, longest_sorted_right)
        i, j = 0, len(arr) - longest_sorted_right
        while i < longest_sorted_left and j < len(arr):
            if arr[i] <= arr[j]:
                answer = max(answer, i + 1 + len(arr) - j)
                i += 1
            else:
                j += 1
        return len(arr) - answer
        