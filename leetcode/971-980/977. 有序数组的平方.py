class Solution:
    def sortedSquares(self, A):
      l = [a*a for a in A]
      l.sort()
      return l

s = Solution()
print(s.sortedSquares([-4,-1,0,3,10]))
print(s.sortedSquares([-7,-3,2,3,11]))