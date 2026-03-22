from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:
        long_len = 0
        count = defaultdict(int)
        for c in s:
            count[c] += 1

        is_one = 0
        for count_char in count.values():
            if count_char % 2 == 1:
                is_one = 1
            long_len += count_char//2 * 2
        return long_len + is_one
                