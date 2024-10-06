import re

#
# @lc app=leetcode id=819 lang=python3
#
# [819] Most Common Word
#


# @lc code=start
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        list_of_words = re.split(r"\W+", paragraph.lower())
        new_list = [w for w in list_of_words if w not in banned and w != ""]
        return max(new_list, key=new_list.count)


# @lc code=end
