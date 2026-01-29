class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        answer = 0
        boxes_queue = deque()
        locked_boxes = set()
        for initial in initialBoxes:
            if status[initial] == 1:
                boxes_queue.append(initial)
            else:
                locked_boxes.add(initial)
        
        all_keys = set()
        while boxes_queue:
            curr_box = boxes_queue.popleft()
            answer += candies[curr_box]
            for new_box in containedBoxes[curr_box]:
                if status[new_box] == 1 or new_box in all_keys:
                    boxes_queue.append(new_box)
                    if new_box in all_keys:
                        all_keys.remove(new_box)
                else:
                    locked_boxes.add(new_box)
            
            curr_keys = keys[curr_box]
            for new_key in curr_keys:
                if new_key in locked_boxes:
                    boxes_queue.append(new_key)
                    locked_boxes.remove(new_key)
                else:
                    all_keys.add(new_key)
        return answer