class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        strs_map = defaultdict(list)
        for word in strs:
            w = "".join(sorted(list(word)))
            strs_map[w].append(word)

        return [w for w in strs_map.values()]
