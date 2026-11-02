class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results_dict = defaultdict(list)

        for s in strs:
            key_arr = [0] * 26

            for c in s:
                key_arr[ord(c) - ord('a')] += 1

            results_dict[tuple(key_arr)].append(s)

        return list(results_dict.values())



















        