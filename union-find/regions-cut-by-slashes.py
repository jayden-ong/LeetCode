class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        # Want to map each area in a square to its parent
        parents = {}
        # Each area can be cut up into four regions
        def find(curr_area):
            # Means this area hasn't been explored yet
            if curr_area not in parents:
                parents[curr_area] = curr_area
                return curr_area
            
            while parents[curr_area] != curr_area:
                curr_area = parents[curr_area]
            return curr_area
        
        def union(area1, area2):
            parent1 = find(area1)
            parent2 = find(area2)
            # This makes both areas have the same top node
            parents[parent1] = parent2
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "\\":
                    union((i, j, 'north'), (i, j, 'east'))
                    union((i, j, 'south'), (i, j, 'west'))
                elif grid[i][j] == "/":
                    union((i, j, 'north'), (i, j, 'west'))
                    union((i, j, 'south'), (i, j, 'east'))
                else:
                    union((i, j, 'north'), (i, j, 'west'))
                    union((i, j, 'south'), (i, j, 'east'))
                    union((i, j, 'north'), (i, j, 'south'))
                
                # Can union east west and north south
                if j > 0:
                    union((i, j - 1, 'east'), (i, j, 'west'))
                
                if i > 0:
                    union((i, j, 'north'), (i - 1, j, 'south'))
            # print(parents)

        # Need to dissect all roots after
        # print(parents)
        all_parents = set()
        for child in parents:
            # Need to find the final parent of all the children
            all_parents.add(find(child))
        return len(all_parents)