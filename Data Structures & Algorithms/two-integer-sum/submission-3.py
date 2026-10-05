class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = [] #list of two ints
        for i, num in enumerate(nums):
            A.append([num, i])
        # initialized an empty array to store ORIGINAL 
        # index and value pair

        sorted_nums = sorted(A) # sorts on first element
        i_index, j_index = 0, len(A)-1

        # iterate thru array until we land on
        # correct two sorted indices
        while (i_index < j_index):
            total = sorted_nums[i_index][0] + sorted_nums[j_index][0]
            if total == target:
                a, b = sorted_nums[i_index][1], sorted_nums[j_index][1]
                return [min(a,b), max(a,b)]
            elif total < target:
                i_index+=1
            else:
                j_index-=1

        # for i, num in enumerate(nums) WHENEVER YOU NEED 
        # BOTH INDEX AND VALUE
        # for i in range (len(nums))