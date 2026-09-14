class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Inp: int array - >  nums, an single int -> K
        nums = [1,1,1,2,2,3] , k = 2

        output: [1,2] 

        the answer seems to output the elements that were the most unique in array

        A set comes to mind for this problem
        first record each element inside of nums.
        anaylze their counts to see which k number of them were duplicated the most inside of nums.
        something about unique
        After further investingating A dict might be the more optimal solution
        """
        import heapq
        count_dict = {}
        heap = []

        for value in nums:
            count_dict[value] = 1 + count_dict.get(value, 0)
        
        for number, count in count_dict.items():
            heapq.heappush(heap, (count, number))

        result = heapq.nlargest(k, heap)
        final_ele = []
        for count, number in result:
            final_ele.append(number)
        return final_ele


# import heapq
# def skyrim_items(weapons, k):
#     loot_heap = []
#     my_dict = {}

#     for name, damage in weapons:
#         heapq.heappush(loot_heap, (damage,name))