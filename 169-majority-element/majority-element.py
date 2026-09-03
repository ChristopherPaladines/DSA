class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Input: given an arr 'nums' of size  n
        # Out:   return the majority element, an element that appears more than half the size of n or the array.
        
        # We must first think what DSA: would most be beneficial
        # We must scan through the entire array

        # set: A set wouldnt be helpful since we need to figure out the majority
        # A hashmap would be the easiest for counting the highest value seen.
        # once we scan, we must see if the count can be counted and compared to see if it's the highest.

        # if using range we can probably compare 1 + 1
      dict_ele = {}
      major_count = 0
      majority_element = 0

      for index, values in enumerate(nums):
        dict_ele[values] = dict_ele.get(values, 0) + 1
        if dict_ele[values] >= major_count:
            major_count = dict_ele[values]
            majority_element = values
      return majority_element


        

