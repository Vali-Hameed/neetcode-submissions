class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        map=defaultdict(int)
        output=[]
        for i in range(len(nums)):
            output.append(nums[i])
        for i in range(len(nums)):
            map[i] = 1
            for j in range(len(nums)):
                if i == j:
                    continue 
                map[i]= map[i]*nums[j]

        return list(map.values())