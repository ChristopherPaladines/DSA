class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
    we have our nums and target parameters,

    our goal is to return the indices that make up

    our target, which are two numbers from the given array when summed == to target'

    we may assume there is exactly one solution, no repeating answwers. Any order return
        """
        dictionary = {}
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in dictionary:
                return dictionary[complement], i
            dictionary[nums[i]] = i