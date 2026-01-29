class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set()
        for letter in allowed:
            allowed_set.add(letter)
        
        answer = 0
        for word in words:
            valid = True
            for char in word:
                if char not in allowed_set:
                    valid = False
                    break
                
            if valid:
                answer += 1
        return answer