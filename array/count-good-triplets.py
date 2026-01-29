class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        # 0 1 1 3 7 9
        length_arr = len(arr)
        answer = 0
        for i in range(length_arr - 2):
            for j in range(i + 1, length_arr - 1):
                for k in range(j + 1, length_arr):
                    if abs(arr[j] - arr[i]) <= a and abs(arr[k] - arr[j]) <= b and abs(arr[k] - arr[i]) <= c:
                        answer += 1
        return answer