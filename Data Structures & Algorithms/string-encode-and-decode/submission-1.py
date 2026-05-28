class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += str((len(s))) + '#' + s
        
        return encoded

    def decode(self, s: str) -> List[str]:

        length = len(s)
        result = []
        index = 0

        while index < length:
            cur_index = index

            while cur_index < length and s[cur_index].isdigit():
                cur_index += 1
            
            strlen = int(s[index:cur_index])

            cur_index += 1

            result.append(s[cur_index: cur_index + strlen])

            index = cur_index + strlen

        return result

        
