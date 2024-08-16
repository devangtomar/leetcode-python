#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for char in t:
            if char not in s or s.count(char) != t.count(char):
                return char
# @lc code=end

