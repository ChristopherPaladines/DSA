class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # given an array 'nums'
        # return true if any element/integer value appears more than once.
        # if every value is unique return false

        # plan we can go through each element and place them in a set
        # if a value is not added into our set its because it already exists and thus returns false
    # nums = [2,3,5]
        seen = set()
        for i in nums:
            if i not in seen:
                seen.add(i)
            else:
                return True
        return False
                


