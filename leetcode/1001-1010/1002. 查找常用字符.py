class Solution:
    def commonChars(self, A):
        minfreq = [float("inf")] * 26
        for word in A:
            freq = [0] * 26
            for ch in word:
                freq[ord(ch) - ord("a")] += 1
            for i in range(26):
                minfreq[i] = min(minfreq[i], freq[i])
        ans = list()
        for i in range(26):
            ans.extend([chr(i + ord("a"))] * minfreq[i])
        return ans


s = Solution()
res = s.commonChars(["bella","label","roller"])
print(res)
res = s.commonChars(["cool","lock","cook"])
print(res)
res = s.commonChars(["acabcddd", "bcbdbcbd", "baddbadb",
                     "cbdddcac", "aacbcccd", "ccccddda", "cababaab", "addcaccd"])
print(res)
