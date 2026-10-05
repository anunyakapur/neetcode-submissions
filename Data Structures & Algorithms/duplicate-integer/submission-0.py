class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False

    # Convert the array into a hash set, which removes duplicates.
    # return len(set(nums)) != len(nums)