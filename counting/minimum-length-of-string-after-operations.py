class Solution:
    def minimumLength(self, s: str) -> int:
        answer = 0
        letters_dict = defaultdict(int)
        for letter in s:
            letters_dict[letter] += 1
            answer += 1
            if letters_dict[letter] == 3:
                answer -= 2
                letters_dict[letter] -= 2
        return answer