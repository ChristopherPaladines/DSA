class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        """
        given an int array ->
        nums of the lengh of size n
        create an array of length 2 of n, ans
        """
        ans = []

        for i in range(len(nums)):
            ans.append(nums[i])
        for i in range(len(nums)):
            ans.append(nums[i])                
        return ans