class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num={}
        for i, n in enumerate(nums):
            num[n]=i

        for i, n in enumerate(nums):
            difference = target-n
            if difference in num and num[difference]!=i:
                return [i,num[difference]]
                

        