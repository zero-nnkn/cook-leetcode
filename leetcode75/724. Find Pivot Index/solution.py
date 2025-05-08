class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Approach 1
        sum_l = 0
        sum_all = sum(nums)
        for i in range(len(nums)):
            sum_r = sum_all - sum_l - nums[i]

            if sum_r == sum_l:
                return i
            else:
                sum_l += nums[i]
        return -1
