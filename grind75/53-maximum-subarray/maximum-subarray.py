class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # Brute-force
        # max_sum = max(nums)
        # for right in range(len(nums)):
        #     if nums[right] <= max_sum and nums[right] < 0:
        #         continue
                
        #     for left in range(right):
        #         if nums[left] > 0:
        #             max_sum = max(max_sum, sum(nums[left:right + 1]))
        # return max_sum

        prefix_max_sum = [0] * len(nums)
        prefix_max_sum[0] = nums[0]
        for right in range(1, len(nums)):
            prefix_max_sum[right] = max(prefix_max_sum[right-1] + nums[right], nums[right])
        return max(prefix_max_sum)

