#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        length = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                break
            length += 1

        return length
# @lc code=end
