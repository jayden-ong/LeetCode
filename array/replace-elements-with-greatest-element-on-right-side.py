class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length_arr = len(arr)
        curr_index = length_arr - 2
        curr_greatest = arr[-1]
        answer = [-1]
        while curr_index > -1:
            answer = [curr_greatest] + answer
            if arr[curr_index] > curr_greatest:
                curr_greatest = arr[curr_index]
            curr_index -= 1
        return answer