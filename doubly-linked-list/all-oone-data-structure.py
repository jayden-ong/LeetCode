class Node:
    def __init__(self, count):
        self.count = count
        self.prev = None
        self.next = None
        self.keys = set()

class AllOne:
    def __init__(self):
        self.max_node = Node(0)
        self.min_node = Node(0)
        self.max_node.next = self.min_node
        self.min_node.prev = self.max_node
        self.values = {}

    def inc(self, key: str) -> None:
        # Can update it - need to remove it from current node and add it to next node
        if key in self.values:
            node_to_update = self.values[key]
            node_to_update.keys.remove(key)
            # Need to introduce a new node
            if self.values[key].next.count != self.values[key].count + 1 or self.values[key].next == self.min_node:                
                old_node = self.values[key]
                new_node = Node(self.values[key].count + 1)
                last_node = self.values[key].next
                old_node.next = new_node
                new_node.prev = old_node
                new_node.next = last_node
                last_node.prev = new_node
                self.values[key] = new_node
            else:
                curr_node = self.values[key].next
                curr_node.keys.add(key)
                self.values[key] = curr_node
            
            if len(node_to_update.keys) == 0:
                next_node = self.values[key]
                prev_node = node_to_update.prev
                prev_node.next = next_node
                next_node.prev = prev_node
        else:
            # Value has to be 1 and don't have to remove any node
            if self.max_node.next.count == 1:
                new_home = self.max_node.next
                self.values[key] = new_home
            else:
                prev_node = self.max_node
                next_node = self.max_node.next
                new_node = Node(1)
                prev_node.next = new_node
                new_node.prev = prev_node
                new_node.next = next_node
                next_node.prev = new_node
                self.values[key] = new_node
        self.values[key].keys.add(key)
        return

    def dec(self, key: str) -> None:
        curr_node = self.values[key]
        curr_node.keys.remove(key)
        # If previous node is the current node - 1, just need to change its home
        if curr_node.prev.count == curr_node.count - 1:
            self.values[key] = curr_node.prev
        else:
            # Have to introduce a new node
            prev_node = curr_node.prev
            next_node = curr_node
            new_node = Node(curr_node.count - 1)
            prev_node.next = new_node
            new_node.prev = prev_node
            new_node.next = next_node
            next_node.prev = new_node
            self.values[key] = new_node
        
        # Remove it
        if len(curr_node.keys) == 0:
            prev_node = self.values[key]
            next_node = curr_node.next
            prev_node.next = next_node
            next_node.prev = prev_node
        self.values[key].keys.add(key)
        if self.values[key].count == 0:
            del self.values[key]
        return

    def getMaxKey(self) -> str:
        # There is nothing between them
        if self.min_node.prev == self.max_node:
            return ""
        
        for answer in self.min_node.prev.keys:
            return answer
        
    def getMinKey(self) -> str:
        if self.max_node.next == self.min_node:
            return ""
        
        for answer in self.max_node.next.keys:
            return answer


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()