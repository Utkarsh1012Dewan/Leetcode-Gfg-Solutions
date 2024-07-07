class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:

        ans = []
        k = k%len(s)

        for r in range(k,len(s)):
            ans.append(s[r])
        for i in range(k):
            ans.append(s[i])

        return "".join(ans)
        