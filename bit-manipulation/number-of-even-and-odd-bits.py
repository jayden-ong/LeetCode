class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        string_n = format(n, "b")[::-1]
        length_n = len(string_n)
        num_even = 0
        num_odd = 0
        for i in range(length_n):
            if string_n[i] == "1":
                if i % 2 == 0:
                    num_even += 1
                else:
                    num_odd += 1
        return [num_even, num_odd]
