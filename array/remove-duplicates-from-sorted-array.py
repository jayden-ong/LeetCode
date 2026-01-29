class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr_check = 0
        curr_count = 0
        curr_list = nums[0:len(nums)]
        for i in range(0, len(curr_list)):
            if i == 0 or curr_check != curr_list[i]:
                curr_check = curr_list[i]
                curr_count += 1
            else:
                nums.remove(curr_list[i])
        return curr_count