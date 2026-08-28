class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # given an array 'nums'
        # return true if any element/integer value appears more than once.
        # if every value is unique return false

        # plan we can go through each element and place them in a set
        # if a value is not added into our set its because it already exists and thus returns false
    # nums = [2,3,5]


# optimal solution based off best runtimes is grabbing the length of nums and comparing it to the length of nums if it was placed inside a set
# the reason it works is because a set kicks out duplicates, so if the lengths differ, we know a duplicate existed. Meaning if the lengths are equal, all elements were unique


# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         # return True if (nums[0]^nums[1])==0 else False
#         return len(nums)!=len(set(nums))
        
        seen = set()
        for i in nums:
            if i not in seen:
                seen.add(i)
            else:
                return True
        return False
                


