# 计算斐波拉契数列
class Solution:
    def fib(self, N: int):
        if N == 0:
          return 0
        elif N == 1:
          return 1
        else:
          return self.fib(N-1) + self.fib(N-2)