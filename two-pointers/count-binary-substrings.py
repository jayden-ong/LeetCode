class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groupings = []
        curr = s[0]
        grouping = 1
        for i in range(1, len(s) + 1):
            if i == len(s) or s[i] != curr:
                groupings.append(grouping)
                if i < len(s):
                    curr, grouping = s[i], 1
            else:
                grouping += 1
        
        answer = 0
        for i in range(1, len(groupings)):
            answer += min(groupings[i - 1], groupings[i])
        return answer
        