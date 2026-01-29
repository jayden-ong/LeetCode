class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        ranges_list = []
        start_range = nums[0]
        end_range = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - end_range != 1:
                # Need to create a new range
                if end_range == start_range:
                    ranges_list.append(str(start_range))
                else:
                    ranges_list.append(str(start_range) + "->" + str(end_range))
                start_range = nums[i]
            end_range = nums[i]

        if end_range == start_range:
            ranges_list.append(str(start_range))
        else:
            ranges_list.append(str(start_range) + "->" + str(end_range))
        return ranges_list