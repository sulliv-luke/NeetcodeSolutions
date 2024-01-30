class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Split multiplication into a left part and a right part
        length = len(nums)
        result = [1] * length
        for i in range(1, length):
            # First, result[i] will always be the product of everything to the left of it
            # For [1,2,3,4] for example, when result will be [1, 1, 2, 6] (the 1 at the start is just because it is unchanged)
            result[i] = result[i-1] * nums[i-1]

        # Init right to the last element of nums
        right = nums[-1]
        for i in range(length-2, -1, -1):
            # Go backwards
            result[i] *= right
            right *= nums[i]

        return result
        



        