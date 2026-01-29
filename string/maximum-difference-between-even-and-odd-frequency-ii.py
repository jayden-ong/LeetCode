class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        answer = float('-inf')
        for a in ['0', '1', '2', '3', '4']:
            for b in ['0', '1', '2', '3', '4']:
                if a == b:
                    continue
                
                a_freq = [0] * (len(s) + 1)
                b_freq = [0] * (len(s) + 1)
                for i in range(1, len(s) + 1):
                    a_freq[i] = a_freq[i - 1] + (a == s[i - 1])
                    b_freq[i] = b_freq[i - 1] + (b == s[i - 1])
                
                best_comb = [[float('-inf'), float('-inf')], [float('-inf'), float('-inf')]]
                j = 0
                for i in range(k, len(s) + 1):
                    while i - j >= k and a_freq[i] > a_freq[j] and b_freq[i] > b_freq[j]:
                        parity1 = a_freq[j] % 2
                        parity2 = b_freq[j] % 2
                        best_comb[parity1][parity2] = max(best_comb[parity1][parity2], b_freq[j] - a_freq[j])
                        j += 1
                    
                    parity1 = a_freq[i] % 2
                    parity2 = b_freq[i] % 2
                    if best_comb[1 - parity1][parity2] != float('-inf'):
                        answer = max(answer, best_comb[1 - parity1][parity2] + (a_freq[i] - b_freq[i]))
                
        if answer == float('-inf'):
            return -1
        return answer