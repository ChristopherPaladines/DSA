class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_elem = {}
        major_count = 0
        majority_num = 0
        # size_n = len(nums)/2
        for index,values in enumerate(nums):
            majority_elem[values] = majority_elem.get(values, 0) + 1
            if majority_elem[values] >= major_count:
                major_count = majority_elem[values]
                majority_num = values
            
            # how do I find the exact key and count and return that value
            # Find a way to return the key of the highest count.
        return majority_num

