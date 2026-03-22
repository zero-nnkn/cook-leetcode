from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # length = 0
        # has_odd = 0
        # for count in Counter(s).values():
        #     length += (count // 2) * 2
        #     if count % 2 == 1:
        #         has_odd = 1
        # return length + has_odd

        length = 0
        for count in Counter(s).values():
            length += (count // 2) * 2
        return length + (length < len(s))
