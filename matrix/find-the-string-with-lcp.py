class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        # No point in investigating the diagonal 
        answer = [""] * len(lcp)
        curr = ord('a')
        for i in range(len(lcp)):
            if answer[i] != "":
                continue
            
            if curr > ord('z'):
                return ""
            answer[i] = chr(curr)
            for j in range(i + 1, len(lcp)):
                if lcp[i][j] > 0:
                    answer[j] = answer[i]
            curr += 1
        
        for i in range(len(lcp) - 1, -1, -1):
            for j in range(len(lcp) - 1, -1, -1):
                # They don't match when they are supposed to
                if answer[i] != answer[j]:
                    if lcp[i][j] > 0:
                        return ""
                else:
                    if i == len(lcp) - 1 or j == len(lcp) - 1:
                        # The maximum length of the substring is 1
                        if lcp[i][j] != 1:
                            return ""
                    else:
                        # lcp[i + 1][j + 1] is the same substring, just remove the first letter
                        # If the second part of the substring doesn't match, it's a fail
                        # We already know the first letter must match
                        if lcp[i][j] != lcp[i + 1][j + 1] + 1:
                            return ""
                    
        return "".join(answer)