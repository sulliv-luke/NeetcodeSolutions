class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Map each number in nums to its index
        map = {}
        for i, num in enumerate(nums):
            # Get the number needed to add to the current number to reach target
            complement = target-num
            # If we've already encountered that number in the list, then return the indices of that number and the current number
            if complement in map:
                return [map[complement], i]
            # Otherwise, store the index of the current number in the map
            map[num] = i
        return [] # If none found