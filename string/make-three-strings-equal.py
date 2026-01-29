class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        smallest_string = min([len(s1), len(s2), len(s3)])
        if [s1[0], s2[0], s3[0]] != [s1[0]] * 3:
            return -1
        
        for i in range(1, smallest_string):
            if [s1[i], s2[i], s3[i]] != [s1[i]] * 3:
                return len(s1) - i + len(s2) - i + len(s3) - i
        return len(s1) - smallest_string + len(s2) - smallest_string + len(s3) - smallest_string