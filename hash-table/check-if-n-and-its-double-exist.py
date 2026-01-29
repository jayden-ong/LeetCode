class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        length_arr = len(arr)
        for i in range(length_arr):
            for j in range(i + 1, length_arr):
                if arr[i] * 2 == arr[j] or arr[j] * 2 == arr[i]:
                    return True
        return False