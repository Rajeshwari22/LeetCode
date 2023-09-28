class Solution:
    def simplifyPath(self, path: str) -> str:
        res=[]
        path=path.split("/")
        for t in path:
            if t=="..":
                if res:
                    res.pop()
            elif t not in ("","."):
                res.append(t)
        return "/"+"/".join(res)
