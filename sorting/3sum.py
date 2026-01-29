class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        num_nums = len(nums)
        if num_nums < 3:
            return []

        curr_list = []
        done_dict = {}
        for i in range(num_nums - 2):
            if nums[i] not in done_dict:
                j = i + 1
                k = num_nums - 1
                while j < k:
                    if nums[i] + nums[j] + nums[k] == 0:
                        curr_list.append([nums[i], nums[j], nums[k]])
                        old_j_val = nums[j]
                        while nums[j] == old_j_val and j < k:
                            j += 1
                    elif nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    else:
                        k -= 1
            done_dict[nums[i]] = True
        return curr_list