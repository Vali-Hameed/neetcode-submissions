class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        length=0
        maxarr=[]
        if len(nums)<1:
            return 0
        first=nums[0]
        for i in range(len(nums)):
            if nums[i]-1 not in nums:
                
                length = 0
                first=nums[i]-1
                length+=1
                while (first+1) in nums:
                    length+=1
                    first+=1
                maxarr.append(length-1)




        return max(maxarr)

