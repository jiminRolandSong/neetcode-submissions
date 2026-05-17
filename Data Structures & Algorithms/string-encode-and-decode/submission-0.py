
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded = encoded + str(len(s)) + '#' + s
        
        return encoded


    def decode(self, s: str) -> List[str]:
        decoded = []
        index = 0
        length = len(s)
        print(length)

        while index < length:
            curindex = index
            #lengthdigit
            while curindex < length and s[curindex].isdigit():
                curindex += 1
            
            print(curindex)
            strlen = int(s[index:curindex])
            #skip delimeter
            curindex += 1

            print(index)
            print(curindex)

            #extract string
            decoded.append(s[curindex:curindex + strlen])

            #move index
            index = curindex + strlen
            print(index)
        
        return decoded