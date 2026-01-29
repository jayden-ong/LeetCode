class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = pow(10, 9) + 7
        letters_list = [0] * 26
        for letter in s:
            # letters_list.append(ord(letter) - 96)
            letters_list[ord(letter) - ord('a')] += 1
        
        for i in range(t):
            curr = [0] * 26
            curr[0] = letters_list[25]
            curr[1] = (letters_list[25] + letters_list[0]) % MOD
            for j in range(2, 26):
                curr[j] = letters_list[j - 1]
            letters_list = curr
        return sum(letters_list) % MOD