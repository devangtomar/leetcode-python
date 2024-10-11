#
# @lc app=leetcode id=728 lang=python3
#
# [728] Self Dividing Numbers
#


# @lc code=start
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right + 1):
            ch = True
            for j in str(i):
                if j != "0":
                    if i % int(j) != 0:
                        ch = False
                else:
                    ch = False
                    break
            if ch:
                res.append(i)
        return res


# @lc code=end
