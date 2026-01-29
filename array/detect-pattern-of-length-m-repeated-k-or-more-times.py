class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        length_arr = len(arr)
        if m > length_arr:
            return False
        
        for i in range(m, length_arr + 1):
            if ((k - 1) * m) + i > length_arr:
                return False

            if arr[i - m:i] * k == arr[i - m:((k - 1) * m) + i]:
                return True
            
        return False