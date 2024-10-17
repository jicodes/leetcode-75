from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            # Process positive and negative asteroids
            while stack and asteroid < 0 < stack[-1]:  # Collision condition
                if stack[-1] < -asteroid:  # Top of the stack is smaller
                    stack.pop()  # Destroy the top asteroid
                    continue
                elif stack[-1] == -asteroid:  # Equal size
                    stack.pop()  # Both destroy each other
                break  # if the top asteroid is bigger, the current asteroid is destroyed, so break
            else:
                stack.append(asteroid)  # Add the asteroid if no collision

        return stack
