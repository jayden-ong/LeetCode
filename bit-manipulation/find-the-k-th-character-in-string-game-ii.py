class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        last_operation = math.ceil(math.log(k, 2)) // 1
        num_chars = 2 ** last_operation
        modifier = 0
        curr_k = k
        curr_operation = last_operation - 1
        while curr_operation >= 0:
            if operations[curr_operation] == 1 and curr_k >= num_chars // 2:
                modifier += 1
            curr_k -= num_chars // 2
            if curr_k == 1:
                break
            num_chars = 2 ** (int(math.log(curr_k - 1, 2)) + 1)
            curr_operation = int(math.log(num_chars, 2) - 1)
        return chr(ord("a") + (modifier % 26))