class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe = set()
        for i in range(0, len(nums)):
            if nums[i] in dupe:
                return True
            dupe.add(nums[i])

        
        return False