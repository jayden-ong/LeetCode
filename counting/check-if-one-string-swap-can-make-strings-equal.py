class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        length_strings = len(s1)
        num_diffs = 0
        for i in range(length_strings):
            if s1[i] != s2[i]:
                if num_diffs == 0:
                    num_diffs += 1
                    # Will perform string swap on first string
                    desired_character = s2[i]
                    actual_character = s1[i]
                elif num_diffs == 1:
                    num_diffs += 1
                    if s1[i] == desired_character and actual_character == s2[i]:
                        continue
                    else:
                        return False
                else:
                    return False
        if num_diffs == 1:
            return False
        return True