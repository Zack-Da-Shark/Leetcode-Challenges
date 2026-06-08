def threeSum(self, nums: list[int]) -> list[list[int]]:
    output = []
    
    nums.sort()
    for x in range(len(nums)):
        seen = {}
        target = -nums[x]

        # Search if any other numbers can go with it with the 2sum answer
        for i in range(x + 1, len(nums)):
            needed = target - nums[i]
            if needed in seen:
                # Add it to the answer list, now how to not add duplicates
                # SORT IT
                add = [nums[x], nums[i], nums[seen[needed]]]
                add.sort()

                # Add it if it's not in
                if add not in output:
                    output.append(add)
            else:
                # Add to the ;dictionasry
                seen[nums[i]] = i
    return output
