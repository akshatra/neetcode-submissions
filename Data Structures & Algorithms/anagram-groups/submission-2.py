class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_dict = defaultdict(list)


        for s in strs:
            count_c = [0] * 26
            
            for c in s:
                count_c[ord(c) - ord('a')] += 1
        
            res_dict[tuple(count_c)].append(s) 

        return list(res_dict.values())



















        