class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for i in strs:
            temp = ''.join(sorted(i))
            anagram_map[temp].append(i)
        return list(anagram_map.values())