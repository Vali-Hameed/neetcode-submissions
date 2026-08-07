class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans=[]
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            difference = 0-nums[i]
            while left<right:
                if nums[left]+nums[right]<difference:
                    left+=1
                elif nums[left]+nums[right]>difference:
                    right-=1
                elif nums[left]+nums[right]==difference:
                    order=[nums[i],nums[left],nums[right]]
                    if order not in ans:
                        ans.append(order)
                    left +=1
                   
        
        return ans



                                                                             