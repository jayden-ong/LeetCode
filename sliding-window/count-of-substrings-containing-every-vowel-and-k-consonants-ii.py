class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def validate_dict(vowels_dict):
            for letter in "aeiou":
                if vowels_dict[letter] <= 0:
                    return False
            return True
        
        def solve(curr_k):
            left = 0
            num_consonants = 0
            vowels_dict = defaultdict(int)
            answer = 0
            for curr_end in range(len(word)):
                if word[curr_end] in "aeiou":
                    vowels_dict[word[curr_end]] += 1
                else:
                    num_consonants += 1
                
                while validate_dict(vowels_dict) and num_consonants >= curr_k:
                    answer += len(word) - curr_end
                    if word[left] in "aeiou":
                        vowels_dict[word[left]] -= 1
                    else:
                        num_consonants -= 1
                    left += 1
            return answer
        
        return solve(k) - solve(k + 1)