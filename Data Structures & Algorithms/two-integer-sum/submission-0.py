class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i,j]
    

    # POTENTIAL APPROACHES
    # double for loop, one at index 0 to len of array
    # second from i+1 to len of array
    # if nums[i]+nums[j] == target:
    #     return [i,j]

