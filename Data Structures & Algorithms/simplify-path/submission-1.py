class Solution:
    def simplifyPath(self, path: str) -> str:
        splited = path.split('/')

        okays = []
        for i in splited:
            current = i

            if len(current) == 0:
                continue

            if len(okays) > 0 and current == "..":
                okays.pop()
            elif current != '.' and current != "..":
                okays.append(current)
        
        return '/' + '/'.join(okays)