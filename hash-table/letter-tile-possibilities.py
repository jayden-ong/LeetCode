class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        possibilities = set()
        tiles_dict = defaultdict(int)
        for tile in tiles:
            tiles_dict[tile] += 1
        
        def find_possibilities(curr_possibility, num_tiles_remaining):
            if curr_possibility != "":
                possibilities.add(curr_possibility)
            
            # We are at the end
            if num_tiles_remaining == 0:
                return
            
            for tile in tiles_dict:
                if tiles_dict[tile] > 0:
                    tiles_dict[tile] -= 1
                    find_possibilities(curr_possibility + tile, num_tiles_remaining - 1)
                    tiles_dict[tile] += 1
            return

        find_possibilities("", len(tiles))
        return len(possibilities)