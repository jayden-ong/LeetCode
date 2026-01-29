class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        bits_set = [0] * 32
        left = 0
        answer = float('inf')

        def update_bits(binary_num, add):
            for i in range(len(binary_num)):
                if binary_num[len(binary_num) - i - 1] == "1":
                    if add:
                        bits_set[31 - i] += 1
                    else:
                        bits_set[31 - i] -= 1
        
        def get_curr_num():
            curr = ""
            for i in range(32):
                if bits_set[i] > 0:
                    curr += "1"
                else:
                    curr += "0"
            return int(curr, 2)

        for i in range(len(nums)):
            right = nums[i]
            # Update the bit counts
            update_bits(format(right, 'b'), True)
            curr_num = get_curr_num()
            while left <= i and curr_num >= k:
                answer = min(answer, i - left + 1)
                # Remove left element
                update_bits(format(nums[left], 'b'), False)
                curr_num = get_curr_num()
                left += 1
        
        if answer == float('inf'):
            return -1
        return answer
        