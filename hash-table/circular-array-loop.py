class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        # If the length is x, going x + 2 is equivalent to going just 2
        # Going negative can be expressed as going forward
        for i in range(len(nums)):
            # -6 // 5 = -1?
            is_negative = False
            if nums[i] < 0:
                is_negative = True
                nums[i] = nums[i] - (nums[i] // len(nums) + 1) * len(nums)
            nums[i] = nums[i] % len(nums)
            if is_negative:
                nums[i] *= -1
        print(nums)
        for i in range(len(nums)):
            positive = nums[i] > 0
            starting_index = i
            curr_ind = i
            for j in range(len(nums)):
                curr_ind = (curr_ind + abs(nums[curr_ind])) % len(nums)
                if (positive and nums[curr_ind] < 0) or (not positive and nums[curr_ind] >= 0):
                    break
                     
                if curr_ind == starting_index:
                    return True
        return False
