class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        output = []

        strssorted = []
        for s in strs:
            strssorted.append("".join(sorted(s)))
        
        strset = set(strssorted)

        for s in strset:
            group = []
            for i in range(len(strs)):
                if strssorted[i] == s:
                    group.append(strs[i])
            output.append(group)
        
        return output

            