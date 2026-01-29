class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occur_dict = {}
        for num in arr:
            if num in occur_dict:
                occur_dict[num] += 1
            else:
                occur_dict[num] = 1
        
        occur_set = set()
        for key in occur_dict:
            if occur_dict[key] in occur_set:
                return False
            else:
                occur_set.add(occur_dict[key])
        return True