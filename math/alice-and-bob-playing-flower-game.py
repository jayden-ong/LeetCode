class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # Count the number of odd sums?
        num_odd_n = math.ceil(n / 2)
        num_odd_m = math.ceil(m / 2)
        num_even_n = n - num_odd_n
        num_even_m = m - num_odd_m
        return num_odd_n * num_even_m + num_odd_m * num_even_n
