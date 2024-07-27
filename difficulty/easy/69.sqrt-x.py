import math

#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        low = 0
        high = x // 2

        while low <= high:
            mid = math.floor((low + high) / 2)
            if (mid * mid) == x:
                return mid
            elif (mid * mid) < x:
                low = mid + 1
            else:
                high = mid - 1
        return high
# @lc code=end
