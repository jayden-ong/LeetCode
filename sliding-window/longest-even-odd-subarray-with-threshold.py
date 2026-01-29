class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        longest = 0
        prev = None
        curr_distance = 0
        for num in nums:
            if num % 2 == 0:
                # Have to restart
                if curr_distance == 0 and num <= threshold:
                    curr_distance += 1
                elif (prev is not None and prev == 0 and curr_distance > 0) or num > threshold:
                    longest = max(longest, curr_distance)
                    if num > threshold:
                        curr_distance = 0
                    else:
                        curr_distance = 1
                else:
                    curr_distance += 1
            else:
                if (prev is not None and prev == 1 and curr_distance > 0) or num > threshold:
                    longest = max(longest, curr_distance)
                    prev = None
                    curr_distance = 0
                elif curr_distance > 0:
                    curr_distance += 1
            prev = num % 2
        return max(longest, curr_distance)
