class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        length_arr = len(arr)
        # [1,2,3,4,5,6]
        # [3,5,6,6,5,3]

        # [1,2,3,4,5,6,7]
        # [4,6,8,8,8,6,4]
        # ends are added (length_arr // 2) + 1 times or (length_arr // 2) rounded up

        # [1,2,3,4,5,6,7,8]
        # [4,7,9,10,10,9,7,4]

        # [1,2,3,4,5,6,7,8,9]
        # [5,7,11,12,13,12,11,7,5]

        answer = 0
        for i in range(0, length_arr, 2):
            subarray_length = i + 1
            for j in range(subarray_length, length_arr + 1):
                answer += sum(arr[j - subarray_length:j])
            #print(answer)
        return answer