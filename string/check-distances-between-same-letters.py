class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        distances_list = [-1] * 26
        i = 0
        for char in s:
            if distances_list[ord(char) - 97] == -1:
                distances_list[ord(char) - 97] = i
            else:
                if i - distances_list[ord(char) - 97] - 1 != distance[ord(char) - 97]:
                    return False
            i += 1
        return True