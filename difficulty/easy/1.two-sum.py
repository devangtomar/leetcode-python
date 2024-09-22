#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        if len(nums) < 2:
            return None
        else:
            for i, num in enumerate(nums):
                complement = target -  num
                if complement in nums_map:
                    return [nums_map[complement], i]
                nums_map[num] = i

# @lc code=end
