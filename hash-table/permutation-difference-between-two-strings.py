class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        # Get position of all letters in "t"
        t_dict = {}
        for i in range(len(t)):
            t_dict[t[i]] = i
        
        answer = 0
        for i in range(len(s)):
            answer += abs(i - t_dict[s[i]])
        return answer