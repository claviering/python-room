class Solution:
    saveList = [0, 1, 2]
    def climbStairs(self, N: int):
      if N >= len(self.saveList):
        res = self.climbStairs(N-1) + self.climbStairs(N-2)
        self.saveList.append(res)
        return res
      else:
        return self.saveList[N]

test = Solution()

print(test.climbStairs(10))