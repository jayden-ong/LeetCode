class Solution:
    def isPalindrome(self, x: int) -> bool:
        strnum = str(x)
        if x < 0:
            return False
        for i in range(0, len(strnum)):
            if strnum[i] != strnum[len(strnum) - 1 - i]:
                return False
        return True