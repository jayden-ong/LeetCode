class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        answer = 0
        arr_set = set(arr.copy())
        pairs_done = set()
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                if arr[i] + arr[j] in arr_set and (arr[i], arr[j]) not in pairs_done:
                    pairs_done.add((arr[i], arr[j]))
                    prev = arr[j]
                    curr = arr[i] + arr[j]
                    streak = 3
                    while prev + curr in arr_set:
                        pairs_done.add((prev, curr))
                        prev, curr = curr, prev + curr
                        streak += 1
                    answer = max(answer, streak)
        return answer