class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Approach 1: Greedy
        # if len(nums) < 3:
        #     return False
        # for i in range(len(nums) - 2):
        #     if nums[i] >= max(nums[i+1:]):
        #         continue
        #     for j in range(i + 1, len(nums) - 1):
        #         if nums[j] <= nums[i] or nums[j] >= max(nums[j+1:]):
        #             continue
        #         return True
        # return False

        # Approach 2: two pointer
        first, second = float('inf'), float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
