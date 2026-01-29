class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first_list = nums[:n]
        second_list = nums[n:]
        answer = []
        for i in range(n):
            answer.append(first_list[i])
            answer.append(second_list[i])
        return answer