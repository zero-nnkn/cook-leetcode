class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Approach 1: Like bubble sort
        # non_zero_pos = len(nums) - 1
        # for i in range(len(nums) - 1, -1, -1):
        #     if nums[i] == 0:
        #         nums[i : non_zero_pos] = nums[i + 1: non_zero_pos + 1] 
        #         nums[non_zero_pos] = 0
        #         non_zero_pos -= 1

        # Approach 2: Two pointer
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
