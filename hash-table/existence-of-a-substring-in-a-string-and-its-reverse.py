class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        all_subs = []
        for i in range(len(s) - 1):
            all_subs.append(s[i] + s[i + 1])
        
        reverse_s = s[::-1]
        for sub in all_subs:
            if sub in reverse_s:
                return True
        return False