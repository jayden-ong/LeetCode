class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # To skip counting a lot of numbers, count how many numbers are between
        # curr number and curr number + 1
        def count_steps(curr_num, next_num):
            num_steps = 0
            while curr_num <= n:
                # Want to count amount of numbers between the two
                # Ex. 1, 2, n = 150
                # 10 - 19, 100 - 150
                num_steps += min(n + 1, next_num) - curr_num
                curr_num *= 10
                next_num *= 10
            return num_steps
        curr_k = k - 1
        curr_num = 1
        while curr_k > 0:
            num_steps = count_steps(curr_num, curr_num + 1)
            if num_steps <= curr_k:
                # We cannot find the desired number in this subtree
                # Skip it
                curr_k -= num_steps
                curr_num += 1
            else:
                # We can find the desired number in this subtree
                # Go deeper
                curr_num *= 10
                curr_k -= 1
        return curr_num