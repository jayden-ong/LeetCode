class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq_dict = {}
        for num in arr:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
        
        largest = -1
        for key in freq_dict:
            if freq_dict[key] == key:
                largest = max(largest, key)
        return largest