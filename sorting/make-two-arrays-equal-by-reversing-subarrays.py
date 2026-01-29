class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target_dict = {}
        for num in target:
            if num in target_dict:
                target_dict[num] += 1
            else:
                target_dict[num] = 1
        
        for num in arr:
            if num not in target_dict or target_dict[num] <= 0:
                return False
            target_dict[num] -= 1
        return True