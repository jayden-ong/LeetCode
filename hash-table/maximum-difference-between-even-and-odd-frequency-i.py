class Solution:
    def maxDifference(self, s: str) -> int:
        frequencies = defaultdict(int)
        for char in s:
            frequencies[char] += 1
        
        max_odd = float('-inf')
        min_even = float('inf')
        for char in frequencies:
            if frequencies[char] % 2 == 1:
                max_odd = max(max_odd, frequencies[char])
            else:
                min_even = min(min_even, frequencies[char])
        return max_odd - min_even
