class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        is_dupli = {}
        for index, value in enumerate(nums):
            if value in is_dupli and abs(index - is_dupli.get(value)) <= k :
                return True
            else:
                is_dupli[value] = index

        return False


