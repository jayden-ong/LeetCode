class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr_set = set()
        prev = 0
        num_skipped = 0
        for num in arr:
            if num_skipped + (num - prev - 1) >= k:
                return prev + (k - num_skipped)
            else:
                num_skipped += (num - prev - 1)
                prev = num
            #print(num_skipped)
        
        return prev + (k - num_skipped)