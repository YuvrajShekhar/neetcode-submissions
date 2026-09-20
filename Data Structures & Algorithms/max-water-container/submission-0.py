class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        output = 0
        
        while left<right:
            volume = min(heights[left],heights[right]) * (right-left)
            output = max(output,volume)

            if(heights[left]>heights[right]):
                right -= 1
            else:
                left+=1

        return output