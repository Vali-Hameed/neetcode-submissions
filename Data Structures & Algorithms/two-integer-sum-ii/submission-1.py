class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(len(numbers)):
            diff=target-numbers[i]
            for j in range(i,len(numbers)):
                if diff == numbers[j] and i!=j:
                    return [i+1,j+1]
        