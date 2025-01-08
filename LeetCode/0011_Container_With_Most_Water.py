class Solution:
    def maxArea(self, height: List[int]) -> int:
        length: int = len(height)
        left: int = 0
        right: int = length - 1
        max_water: int = 0

        for i in range(length):
            base = right - left
            water = base * height[left] if height[left] < height[right] else base * height[right]
            if water > max_water:
                max_water = water
            # max_water = max(max_water, base * height[left] if height[left] < height[right] else base * height[right])
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water

        
