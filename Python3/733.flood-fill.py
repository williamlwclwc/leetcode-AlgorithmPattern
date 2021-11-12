#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def _floodfill(image, sr, sc, newColor, oldColor):
            if not 0 <= sr < len(image) or not 0 <= sc < len(image[0]):
                return
            if image[sr][sc] == oldColor:
                image[sr][sc] = newColor
            else:
                return
            _floodfill(image, sr+1, sc, newColor, oldColor)
            _floodfill(image, sr-1, sc, newColor, oldColor)
            _floodfill(image, sr, sc+1, newColor, oldColor)
            _floodfill(image, sr, sc-1, newColor, oldColor)
        # if current color == new color: infinite loop
        if image[sr][sc] != newColor:
            _floodfill(image, sr, sc, newColor, image[sr][sc])
        return image
# @lc code=end

