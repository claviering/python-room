class Solution:
    def genString(self, s, stringLen, K):
        if stringLen == 1:
          return s
        center = stringLen / 2
        if K - 1 >= center:
          s = "1" if s == "0" else "0"
          K = K - center
        else:
          s = "0" if s == "0" else "1"
        return self.genString(s, center, K)
    def kthGrammar(self, N: int, K: int):
        return self.genString("0", 2**(N-1), K)

test = Solution()
# print(test.kthGrammar(1, 1))
print(test.kthGrammar(2, 1))
# print(test.kthGrammar(2, 2))
# print(test.kthGrammar(4, 5))