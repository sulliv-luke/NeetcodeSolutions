class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        map = {}
        for num in nums:
            if not num in map:
                map[num] = 1
            else:
                map[num] += 1
        
        # The key parameter of the sorted function uses a lambda function to sort the items based on their frequency 
        # (x[1] refers to the value part of each tuple
        sorted_map_items = sorted(map.items(), key=lambda x:x[1])
        
        # Extracts the last k elements from sorted_map_items since these are the ones with the highest frequencies. 
        # It then retrieves the original numbers (the first element of each tuple, item[0]) and returns them as a list.
        return [item[0] for item in sorted_map_items[len(sorted_map_items)-k:]]
    
if __name__ == '__main__':
    solution = Solution()
    assert solution.topKFrequent([1,1,1,2,2,3], 2) == [1, 2] or [2,1], "Test case 1 failed"
    assert solution.topKFrequent([1], 1) == [1], "Test case 2 failed"
    print("All test cases passed")