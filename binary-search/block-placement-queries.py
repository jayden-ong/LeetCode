class SegTree:
    def __init__(self):
        self.max = pow(10, 4) * 5
        self.segment = [0] * (self.max << 2)
        self.sorted_list = SortedList([0, self.max])
    
    def update(self, index, val, position, left, right):
        if left == right:
            self.segment[position] = val
            return
        
        mid = (left + right) // 2
        if index <= mid:
            self.update(index, val, position << 1, left, mid)
        else:
            self.update(index, val, position << 1 | 1, mid + 1, right)
        
        self.segment[position] = max(self.segment[position << 1], self.segment[position << 1 | 1])
    
    def query(self, far_left, far_right, position, left, right):
        if far_left <= left and right <= far_right:
            return self.segment[position]
        
        mid = (left + right) // 2
        answer = 0
        if far_left <= mid:
            answer = max(answer, self.query(far_left, far_right, position << 1, left, mid))
        if far_right > mid:
            answer = max(answer, self.query(far_left, far_right, position << 1 | 1, mid + 1, right))
        
        return answer

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        segment_tree = SegTree()
        segment_tree.update(segment_tree.max, segment_tree.max, 1, 0, segment_tree.max)
        answer = []

        for query in queries:
            if query[0] == 1:
                x = query[1]
                index = min(len(segment_tree.sorted_list) - 1, segment_tree.sorted_list.bisect_right(x))
                right = segment_tree.sorted_list[index]
                if index > 0:
                    left = segment_tree.sorted_list[index - 1]
                else:
                    left = segment_tree.sorted_list[0]
                
                segment_tree.update(x, x - left, 1, 0, segment_tree.max)
                segment_tree.update(right, right - x, 1, 0, segment_tree.max)
                segment_tree.sorted_list.add(x)
            else:
                x, sz = query[1], query[2]
                index = min(len(segment_tree.sorted_list) - 1, segment_tree.sorted_list.bisect_right(x))
                if index == 0:
                    pre = segment_tree.sorted_list[0]
                else:
                    pre = segment_tree.sorted_list[index - 1]
                
                largest_space = max(x - pre, segment_tree.query(0, pre, 1, 0, segment_tree.max))
                answer.append(largest_space >= sz)

        return answer
