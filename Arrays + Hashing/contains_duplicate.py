class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        map = {}
        for num in nums:
            if num in map:
                return True
            else:
                map[num] = 1
        return False
    
if __name__ == '__main__':
    solution = Solution()
    assert not solution.containsDuplicate([1,2,3,4]), "Test case 1 failed"
    assert solution.containsDuplicate([1,1,2,3,4]), "Test case 2 failed"
    assert not solution.containsDuplicate([]), "Test case 3 failed"
    assert not solution.containsDuplicate([1]), "Test case 4 failed"
    assert solution.containsDuplicate([1,1]), "Test case 5 failed"
    print("All test cases passed")