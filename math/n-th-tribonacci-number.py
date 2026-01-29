class Solution:
    def tribonacci(self, n: int) -> int:
        trib_dict = {}
        for i in range(n + 1):
            if i == 0:
                trib_dict[i] = 0
            elif i == 1:
                trib_dict[i] = 1
            elif i == 2:
                trib_dict[i] = 1
            else:
                trib_dict[i] = trib_dict[i - 3] + trib_dict[i - 2] + trib_dict[i - 1]
        return trib_dict[n]