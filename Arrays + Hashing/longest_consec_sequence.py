
class Solution(object):
    def longestConsecutive(self, nums):
        s, longest = set(nums), 0
        for num in s:
            if num - 1 in s: continue # This skips numbers we have already visited before
            j = 1
            while num + j in s: j+=1 # While the next number in the sequence is present in the set, increase the counter
            longest=  max(longest, j) # If the counter is greater than the length of the current longest sequence, then make that the new longest sequence length
        return longest


    

if __name__ == "__main__":
    sol = Solution()
    nums = [100,4,200,1,3,2]
    sol.longestConsecutive(nums)



            