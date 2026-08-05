class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results=[]
        
        for i in range(len(temperatures)):
            max=True
            count = 0
            current = temperatures[i]
            for j in range(i+1,len(temperatures)):
                if current < temperatures[j]:
                    count = j-i
                    results.append(count)
                    max=False
                    break
            if max:
                results.append(0)
            


        return results
