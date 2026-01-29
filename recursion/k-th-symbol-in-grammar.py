class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        answer_list = []
        while k > 1:
            answer_list.append(k)
            if k % 2 == 1:
                k //= 2
                k += 1
            else:
                k //= 2
        
        curr = 0
        for i in range(len(answer_list) - 1, -1, -1):
            if curr == 0 and answer_list[i] % 2 == 0:
                curr = 1
            elif curr == 1 and answer_list[i] % 2 == 0:
                curr = 0
        return curr
