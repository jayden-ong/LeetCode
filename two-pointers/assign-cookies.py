class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Want to assign the smallest cookie to the children with the lowest greed
        g.sort()
        s.sort()
        num_kids = len(g)
        num_cookies = len(s)
        i = 0
        j = 0
        kids_happy = 0
        while i < num_kids and j < num_cookies:
            if g[i] <= s[j]:
                i += 1
                kids_happy += 1
            j += 1
        return kids_happy