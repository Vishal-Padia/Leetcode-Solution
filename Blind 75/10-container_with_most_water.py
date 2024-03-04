class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Naive Appraoch
        # area = 0 # Initialize area to 0
        # n = len(height)
        # for i in range(n): # run a for loop in the range of length of heights
        #     for j in range(i+1, n): # run a inner for loop in the range of (i+1,n)
        #         area = max(area, min(height[j], height[i]) * (j-i)) # update the area with the max of area and minimum of height[j], height[i] multiplied by (j-i)

        # return area

        # Better Approach
        area = 0  # Initialize area to 0
        l = 0  # Initialize l to 0
        r = len(height) - 1  # Initialize r to len(height) - 1

        while l < r:  # while l is less than r
            area = max(
                area, min(height[l], height[r]) * (r - l)
            )  # update the area to the max of area and minimum of height[l], height[r] multiplied by (r-1)

            if height[l] < height[r]:  # check if the height[l] is less than height[r]
                l += 1  # if it is, then increment l by 1
            else:
                r -= 1  # if not then decrement r by 1

        return area
