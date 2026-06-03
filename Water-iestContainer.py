class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Simple solution,1 while loop, double pointers!
        biggest = 0
        pos1 = 0
        pos2 = len(height) - 1
        while pos1 < pos2:
            if height[pos2] > height[pos1]:
                possible = height[pos1] * (pos2 - pos1)
                pos1 += 1
                if possible > biggest:
                    biggest = possible
            else:
                possible = height[pos2] * (pos2 - pos1)
                pos2 -= 1
                if possible > biggest:
                    biggest = possible
        return biggest

        # TIME LIMIT EXCEEDED
