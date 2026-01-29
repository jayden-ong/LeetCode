class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_dict = {}
        arr2_set = set(arr2)
        remaining = []
        for num in arr1:
            if num in arr1_dict:
                arr1_dict[num] += 1
            else:
                arr1_dict[num] = 1
            
            if num not in arr2_set:
                remaining.append(num)
        
        curr_answer = []
        for num in arr2:
            curr_answer += [num] * arr1_dict[num]
        remaining.sort()
        return curr_answer + remaining