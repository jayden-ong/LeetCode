class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters_dict = defaultdict(list)
        for i, letter in enumerate(s):
            letters_dict[letter].append(i)
        
        answer = set()
        for letter in letters_dict:
            if len(letters_dict[letter]) >= 2:
                for i in range(letters_dict[letter][0] + 1, letters_dict[letter][-1]):
                    if letter + s[i] + letter not in answer:
                        answer.add(letter + s[i] + letter)

        return len(answer)