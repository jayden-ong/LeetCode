class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        conflict_pairs_heap = []
        for i, (start, end) in enumerate(conflictingPairs):
            heapq.heappush(conflict_pairs_heap, (-min(start, end), max(start, end), i))

        first_block = [-1] * n
        second_block = [-1] * n
        index_block = [-1] * n
        valid_conflict_pairs_heap = []
        for i in range(n - 1, -1, -1):
            while conflict_pairs_heap and -conflict_pairs_heap[0][0] == i + 1:
                _, end, index = heapq.heappop(conflict_pairs_heap)
                heapq.heappush(valid_conflict_pairs_heap, (end, index))

            if len(valid_conflict_pairs_heap) >= 1:
                first_block[i] = valid_conflict_pairs_heap[0][0]
                index_block[i] = valid_conflict_pairs_heap[0][1]
            
            if len(valid_conflict_pairs_heap) >= 2:
                temp = heapq.heappop(valid_conflict_pairs_heap)
                second_block[i] = valid_conflict_pairs_heap[0][0]
                heapq.heappush(valid_conflict_pairs_heap, temp)
        #print(first_block)
        #print(second_block)
        #print(index_block)
        # Want to count how many extra spaces would open up if we remove each pair
        most_removals = defaultdict(int)
        curr_answer = 0
        best_cand = float('-inf')
        for i in range(len(first_block)):
            # No conflict -- removing pair doesn't add more answers
            if first_block[i] == -1:
                curr_answer += n - i
                continue
            elif first_block[i] > -1 and second_block[i] == -1:
                curr_answer += first_block[i] - i - 1
                # Removing a pair would create more answers
                most_removals[index_block[i]] += n - first_block[i] + 1
                best_cand = max(best_cand, most_removals[index_block[i]])
            else:
                curr_answer += first_block[i] - i - 1
                most_removals[index_block[i]] += second_block[i] - first_block[i]
                best_cand = max(best_cand, most_removals[index_block[i]])
        return curr_answer + best_cand