#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#


# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        def get_next_num(n: int) -> int:
            output = 0
            while n:
                digit = n % 10
                output += digit**2
                n = n // 10
            return output

        while n not in visit:
            visit.add(n)
            n = get_next_num(n)
            if n == 1:
                return True
        return False


# @lc code=end
