class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        map_s,map_t = {},{}
        
        for i in range(len(s)):
            map_s[s[i]] = 1 + map_s.get(s[i],0)
            map_t[t[i]] = 1 + map_t.get(t[i],0)

        for k in map_s:
            if map_s[k] != map_t.get(k,0):
                return False
        
        return True

