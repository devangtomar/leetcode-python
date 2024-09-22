#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        answer = 0
        for i in range(len(s)): # IV
            if i < len(s) - 1 and roman[s[i]] < roman[s[i+1]]:
                answer =  answer - roman[s[i]]
            else:
                answer = answer + roman[s[i]]

        return answer

# @lc code=end

