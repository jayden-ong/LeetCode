class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        length_arr = len(arr)
        if length_arr < 3:
            return False
        found_increasing = False
        found_decreasing = False
        for i in range(1, length_arr):
            if arr[i - 1] < arr[i]:
                if not found_increasing:
                    found_increasing = True
                elif found_decreasing:
                    return False
            elif arr[i - 1] > arr[i]:
                if not found_increasing:
                    return False
                elif not found_decreasing:
                    found_decreasing = True
            else:
                return False
        return found_increasing and found_decreasing