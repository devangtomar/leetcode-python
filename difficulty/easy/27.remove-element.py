#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#


# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(0, len(nums)):
            if val != nums[i]:
                nums[index] = nums[i]
                index += 1

        return index


# @lc code=end
