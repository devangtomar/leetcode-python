#
# @lc app=leetcode id=709 lang=python3
#
# [709] To Lower Case
#


# @lc code=start
class Solution:
    def toLowerCase(self, s: str) -> str:
        lower_case = []
        for char in s:
            if "A" <= char <= "Z":
                lower_case.append(chr(ord(char) + 32))
            else:
                lower_case.append(char)
        return "".join(lower_case)


# @lc code=end
