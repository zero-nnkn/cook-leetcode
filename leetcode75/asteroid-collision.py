class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # final_asteroids = [asteroids[0]]
        # for asteroid in asteroids[1:]:
        #     prev_asteroid = final_asteroids.pop(-1)
        #     if prev_asteroid * asteroid > 0:
        #         final_asteroids.append(prev_asteroid)
        #         final_asteroids.append(asteroid)
        #     else:
        #         while prev_asteroid * asteroid <= 0 and prev_asteroid:
        #             diff = prev_asteroid + asteroid
        #             if diff == 0:
        #                 break
        #             else:
        #                 if diff * prev_asteroid >= 0:
        #                     final_asteroids.append(prev_asteroid)
        #                 else:
        #                     prev_asteroid = final_asteroids.pop(-1)
                
        #         if prev_asteroid is None:
        #             final_asteroids.append(asteroid)
        # return final_asteroids

        stack = []
        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                prev = stack[-1]

                if prev + asteroid < 0:
                    stack.pop()
                elif prev + asteroid == 0:
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(asteroid)
        return stack
                    
