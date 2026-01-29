class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = 10 ** 9 + 7
        curr = 1
        letters_list = []
        for i in range(1, len(word) + 1):
            if i == len(word) or word[i] != word[i - 1]:
                letters_list.append((curr, word[i - 1]))
                curr = 1
            else:
                curr += 1
        
        # Count how many different strings there could be
        answer = 1
        for freq, curr_letter in letters_list:
            answer = answer * freq % MOD
        
        # We can remove any amount of letters from any continuous string and still have the min length
        if len(letters_list) >= k:
            return answer
        
        f, g = [1] + [0] * (k - 1), [1] * k
        for i in range(len(letters_list)):
            new_f = [0] * k
            for j in range(1, k):
                new_f[j] = g[j - 1]
                if j - letters_list[i][0] - 1 >= 0:
                    new_f[j] = (new_f[j] - g[j - letters_list[i][0] - 1]) % MOD
            new_g = [new_f[0]] + [0] * (k - 1)
            for j in range(1, k):
                new_g[j] = (new_g[j - 1] + new_f[j]) % MOD
            
            f, g = new_f, new_g
        return (answer - g[k - 1]) % MOD