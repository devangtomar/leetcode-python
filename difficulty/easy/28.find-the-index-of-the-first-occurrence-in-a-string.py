#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#


# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        need_len = len(needle)
        hay_len = len(haystack)
        for i in range(hay_len - need_len + 1):
            if haystack[i : i + need_len] == needle:
                return i
        return -1


# @lc code=end
