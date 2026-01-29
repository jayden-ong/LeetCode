class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        length_arr = len(arr)
        temp = []
        i = 0
        num_elements = 0
        while i < length_arr and num_elements < length_arr:
            if arr[i] == 0:
                temp.append(arr[i])
                temp.append(arr[i])
                num_elements += 2
            else:
                temp.append(arr[i])
                num_elements += 1
            i += 1
        
        for i in range(length_arr):
            arr[i] = temp[i]
