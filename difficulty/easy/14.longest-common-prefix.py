#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#


# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        for i in range(len(min(strs))):
            s = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i] != s:
                    return output
            output += s

        return output


# @lc code=end
