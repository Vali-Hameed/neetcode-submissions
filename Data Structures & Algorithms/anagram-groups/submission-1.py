class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)

        for s in strs:
            
        # Sort the string to create a canonical key for anagrams
        # For example, 'eat', 'tea', and 'ate' all become 'aet'
            sorted_s = "".join(sorted(s))
        
        # Append the original string to the list for that key
            anagram_groups[sorted_s].append(s)

    # Return the values of the dictionary, which are the grouped anagrams
        return list(anagram_groups.values())

