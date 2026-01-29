class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        curr_asteroids = []
        for asteroid in asteroids:
            if asteroid > 0:
                curr_asteroids.append(asteroid)
            else:
                if len(curr_asteroids) == 0 or curr_asteroids[-1] < 0:
                    curr_asteroids.append(asteroid)
                else:
                    is_broken = False
                    while curr_asteroids and curr_asteroids[-1] > 0:
                        # Both are destroyed
                        if abs(curr_asteroids[-1]) == abs(asteroid):
                            curr_asteroids.pop()
                            is_broken = True
                            break
                        elif abs(curr_asteroids[-1]) > abs(asteroid):
                            is_broken = True
                            break
                        else:
                            curr_asteroids.pop()
                    
                    if not is_broken:
                        curr_asteroids.append(asteroid)
                        
        return curr_asteroids