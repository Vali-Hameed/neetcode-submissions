class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        items=defaultdict(list)
        for i in range(len(strs)):
            sorted_s="".join(sorted(strs[i]))
            items["".join(sorted(strs[i]))].append(strs[i])

        return list(items.values())


            