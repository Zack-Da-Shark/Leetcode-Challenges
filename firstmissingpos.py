class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Convert it to a set

        stuff = set(nums)
        # Sets are a=seemingly better than lists
        
        count = 1
        while count in stuff:
            count += 1
        return count
