class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = 1
        left = 0
        max_count = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                if k > 0:
                    k -= 1
                else:
                    while nums[left] != 0 and left < right:
                        left += 1
                    left += 1

            max_count = max(max_count, right - left + 1)
        return max_count - 1
