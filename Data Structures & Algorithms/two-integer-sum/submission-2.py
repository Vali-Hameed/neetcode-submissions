class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        items = {}
        for i in range(len(nums)):
            items[nums[i]]=i

        for i in range(len(nums)):
            difference = target-nums[i]
            if difference in items and i != items[difference]:
                return sorted([i,items[difference]])