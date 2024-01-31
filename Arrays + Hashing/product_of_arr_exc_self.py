class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        """Approach:
            Essentially, here we are reusing calculations that we have already made
            We first multiply everything in the array by the number to the left of it (obviously ignoring the first element)
            Then we go backwards, multiplying everything in the array by the number to the right of it
            Therefore, we get a time complexity of O(N), where N is the length of the array
        """
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
    

if __name__ == "__main__":
    sol = Solution()
    # Define a test list
    test_list = [1, 2, 3, 4]

    # Call the productExceptSelf method with the test list
    result = sol.productExceptSelf(test_list)

    # Print the result
    print(result)
        



        