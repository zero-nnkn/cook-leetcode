class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        final_asteroids = [asteroids[0]]
        for asteroid in asteroids[1:]:
            prev_asteroid = final_asteroids.pop(-1)
            if prev_asteroid * asteroid > 0:
                final_asteroids.append(prev_asteroid)
                final_asteroids.append(asteroid)
            else:
                while prev_asteroid * asteroid <= 0:
                    if prev_asteroid + asteroid == 0:
                        break
                    elif abs(prev_asteroid) < abs(asteroid):
                        prev_asteroid = final_asteroids.pop(-1)
                    else:
                        final_asteroids.append(prev_asteroid)
                        break
        return final_asteroids
