class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        first_edge = edges[0]
        second_edge = edges[1]
        if first_edge[0] in second_edge:
            return first_edge[0]
        return first_edge[1]