class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # If the number we see matches its index, add a chunk
        # Otherwise, we need to increase our chunk to at least arr[i]
        answer = 0
        min_destination = None
        for i in range(len(arr)):
            if min_destination is None:
                if arr[i] == i:
                    answer += 1
                else:
                    min_destination = arr[i]
            else:
                min_destination = max(min_destination, arr[i])
                if min_destination == i:
                    answer += 1
                    min_destination = None
        return answer