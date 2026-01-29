class Tree:
    def __init__(self):
        self.serial = ""
        self.children = {}
        
class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = Tree()
        for path in paths:
            curr = root
            for node in path:
                # We want to create a new subtree and transition to it because there could be more nodes
                if node not in curr.children:
                    curr.children[node] = Tree()
                curr = curr.children[node]

        freq_dict = defaultdict(int)
        def represent_paths(root):
            if len(root.children) == 0:
                return
            
            serial_rep = []
            for child, child_tree in root.children.items():
                represent_paths(child_tree)
                serial_rep.append(child + "(" + child_tree.serial + ")")
            serial_rep.sort()
            root.serial = "".join(serial_rep)
            freq_dict[root.serial] += 1
        
        represent_paths(root)
        answer = []
        curr_path = []
        def detect(root):
            if freq_dict[root.serial] > 1:
                return
            
            if len(curr_path) != 0:
                # To avoid changes being made by the mutable variable
                answer.append(curr_path[:])
            
            for child, child_tree in root.children.items():
                curr_path.append(child)
                detect(child_tree)
                curr_path.pop()
        
        detect(root)
        return answer