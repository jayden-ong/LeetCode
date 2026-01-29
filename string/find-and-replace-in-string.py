class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        answer = ""
        replacements_heap = []
        for i in range(len(indices)):
            heapq.heappush(replacements_heap, (indices[i], sources[i], targets[i]))
        
        prev_index = 0
        while replacements_heap:
            curr_index, curr_source, curr_target = heapq.heappop(replacements_heap)
            if s[curr_index:curr_index + len(curr_source)] == curr_source:
                if curr_index > prev_index:
                    answer += s[prev_index:curr_index]
                answer += curr_target
                prev_index = curr_index + len(curr_source)
        answer += s[prev_index:]
        return answer