class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        count = sum([1 for c in s[:k] if c in vowels])
        max_count = count

        for i in range(1, len(s) - k + 1):
            if s[i - 1] in vowels:
                count -= 1
            if s[i + k - 1] in vowels:
                count += 1
            if count > max_count:
                max_count = count

        return max_count
         