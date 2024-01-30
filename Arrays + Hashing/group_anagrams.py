from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Create a dictionary to store the values of each word in strs, sorted alphabetically
        
        # The functionality of both dictionaries and defaultdict are almost same except for the fact that defaultdict never raises a KeyError. 
        # It provides a default value for the key that does not exist
        map = defaultdict(list)
        for word in strs:
            # Sort the string alphabetically and store the original string in the vector associated to its sorted value
            sorted_str = ''.join(sorted(word))
            map[sorted_str].append(word)
        return list(map.values())

    
if __name__ == '__main__':
    solution = Solution()
    assert solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]], "Test case 1 failed"
    assert solution.groupAnagrams([""]) == [[""]], "Test case 2 failed"
    assert solution.groupAnagrams(["a"]) == [["a"]], "Test case 3 failed"
    print("All test cases passed")



