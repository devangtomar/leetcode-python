#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            result.append(chr(remainder + 65))
            columnNumber //= 26
        return ''.join(reversed(result))

# @lc code=end

