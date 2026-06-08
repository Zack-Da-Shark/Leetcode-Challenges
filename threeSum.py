class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        output = []
        nums.sort()
        
        for i in range(len(nums)):
            # Skip duplicate
            if i > 0 and nums[i-1] == nums[i]:
                continue 
            start = i + 1
            end = len(nums) -1
            
            while(start < end):
                answer = nums[i] + nums[start] + nums[end]
                if answer == 0:
                    # Direct Match
                    # Check if it alread is in
                    add = [nums[i], nums[start], nums[end]]
                    output.append(add)
                    end -= 1
                    while end > start and end < len(nums) - 1 and nums[end] == nums[end + 1]:
                        # Answer is too big
                        # Now need to skip duplicates
                        print("Skipping duplicate on the end")
                        end -= 1
                    start += 1
                    while start < end and nums[start] == nums[start - 1]:
                        # Answer is too small
                        print("Skipping duplicate on the start")
                        start += 1
                    
                elif answer > 0:
                    end -= 1
                    while end > start and end < len(nums) - 1 and nums[end] == nums[end + 1]:
                        # Answer is too big
                        # Now need to skip duplicates
                        print("Skipping duplicate on the end")
                        end -= 1
                else:
                    start += 1
                    while start < end and nums[start] == nums[start - 1]:
                        # Answer is too small
                        print("Skipping duplicate on the start")
                        start += 1
        
        return output
