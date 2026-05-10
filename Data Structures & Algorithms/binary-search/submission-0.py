class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        mid=(l+r)/2
        found = False
        if target in nums:
            while found==False:
                mid=int((l+r)/2)
                if nums[mid] == target:
                    return mid
                    found == True
                if nums[mid]>target:
                    r=mid-1
                if nums[mid]<target:
                    l=mid+1
        else:
            return -1


         
        