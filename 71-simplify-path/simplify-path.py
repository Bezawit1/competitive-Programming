class Solution(object):
    def simplifyPath(self, path):
        stack = []
        pathdirect = path.split("/")
        for i in pathdirect:
            if i == "." or not i:
                continue
            elif i == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return "/" + "/".join(stack)

                    
            