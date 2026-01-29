class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        left = 0
        right = 1
        answer = 0
        # Function that checks whether array is a subarray
        def check(subarray, main_list):
            sub_length = len(subarray)
            for i in range(len(main_list) - sub_length + 1):
                if main_list[i] == subarray[0] and main_list[i:i + sub_length] == subarray:
                    return True
            return False

        while right <= len(nums1) and right - left <= len(nums2):
            print(left)
            print(right)
            print('---')
            if not check(nums1[left:right], nums2):
                left += 1
            else:
                answer = max(answer, right - left)
            right += 1
        return answer
