class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        curr_list = []
        num_nums = len(nums)
        if num_nums < 4:
            return curr_list
        
        # -2, -1, 0, 0, 1, 2
        done_dict_ij = {}
        for i in range(num_nums - 3):
            for j in range(i + 1, num_nums - 2):
                if (nums[i], nums[j]) not in done_dict_ij:
                    k = j + 1
                    l = num_nums - 1
                    while k < l:
                        curr_res = nums[i] + nums[j] + nums[k] + nums[l]
                        if curr_res == target:
                            curr_list.append([nums[i], nums[j], nums[k], nums[l]])
                            old_val = nums[k]
                            while k < l and old_val == nums[k]:
                                k += 1
                        elif curr_res < target:
                            k += 1
                        else:
                            l -= 1
                done_dict_ij[(nums[i], nums[j])] = True
        return curr_list