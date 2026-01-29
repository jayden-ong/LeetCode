class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainders_dict = defaultdict(int)
        num_left = 0
        for num in arr:
            remainder = num % k
            desired = (k - remainder) % k
            if remainders_dict[desired] > 0:
                remainders_dict[desired] -= 1
                num_left -= 1
            else:
                remainders_dict[remainder] += 1
                num_left += 1
        
        return num_left == 0

