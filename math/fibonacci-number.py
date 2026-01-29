class Solution:
    def fib(self, n: int) -> int:
        fib_dict = {}
        for i in range(n + 1):
            if i == 0:
                fib_dict[i] = 0
            elif i == 1:
                fib_dict[i] = 1
            else:
                fib_dict[i] = fib_dict[i - 1] + fib_dict[i - 2]
        return fib_dict[n]