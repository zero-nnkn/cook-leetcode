# Write your solution here
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0

        # Approach 1: Brute force
        # for i in range(len(nums) - 1):
        #     if nums[i] == -1:
        #         continue
        #     for j in range(i + 1, len(nums)):
        #         if nums[j] == -1:
        #             continue
        #         if nums[i] + nums[j] == k:
        #             count += 1
        #             nums[i] = nums[j] = -1
        #             break
        # return count

        # Approach 2
        nums = sorted(nums)
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == k:
                count += 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] < k:
                l += 1
            else:
                r -= 1
        return count
