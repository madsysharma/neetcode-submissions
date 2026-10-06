class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            chars = tuple(list(sorted([c for c in s])))
            if chars not in anagrams:
                anagrams[chars] = [s]
            else:
                anagrams[chars].append(s)
        
        results = []
        for k, v in anagrams.items():
            results.append(anagrams[k])
        return results