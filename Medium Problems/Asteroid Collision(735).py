class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:

            while stack and stack[-1] > 0 and asteroid < 0:

                if abs(stack[-1]) > abs(asteroid): #asteroid can't destroy:
                    break

                elif abs(stack[-1]) == abs(asteroid): #asteroid and last element destroy each other
                    stack.pop()
                    break 

                else: #asteroid destroys last element
                    stack.pop()
                





            
            else:
                stack.append(asteroid)


        return stack
        