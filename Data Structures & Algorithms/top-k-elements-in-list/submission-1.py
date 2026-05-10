class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=defaultdict(int)
        list=[[] for i in range(len(nums) + 1)]
        for n in nums:
            freq[n]+=1

        for n, c in freq.items():
            list[c].append(n)
        res=[]
        for i in range(len(list)-1,0,-1):
            for n in list[i]:
                res.append(n)
                if len(res)==k:
                    return res

