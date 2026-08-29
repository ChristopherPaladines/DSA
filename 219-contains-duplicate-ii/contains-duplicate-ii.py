class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # given arr nums and in an int k
        # return true if there are two unique indices in the array. so that nums[i] == nums[j] and abs(i - j) <= k
        #  nums[i] == nums[j] is basically saying both indices where the values equal eachother
        #example nums [1,2,3,1,2,3], k = 2  
          #  nums[i] = 1
         #   nums[k] = 2
         # abs (0 - 3) <= 2 - > 3 <= 2 False

         # how to solve this lets think about of DSA
         

        ### ***   Brute force approach is not working because inputs are too large *** ####
        #  for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j] and abs(i - j) <= abs(k):
        #             return True
        #  return False
        is_dupli = {}
        for index, value in enumerate(nums):
            if value in is_dupli and abs(index - is_dupli.get(value)) <= k:
                return True
            else:
                is_dupli[value] = index
        return False
        