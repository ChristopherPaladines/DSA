class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    # Understand: given an array -> [1,2,3] int values
    #             given an int target
    # Return two int indices of the int values that make up target
    # cannot use the same element twice, aka int value.

#1   pass through the entire array

#2   brute force method - > subtract each value by the target
#3   target ex: 7  [1,2,3,4,5,6,7] - >  --  1 > [0] 1-7 = 6 + [0]  1 = 7 target return [0] and [5]
    #3 if the subtracted value by the target: ex 6 + each value in the array equals target return indices

        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j