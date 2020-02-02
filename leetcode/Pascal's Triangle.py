# class Solution:
#     def generateList(self, list: list):
#       return [1] + [list[i] + list[i + 1] for i in range(len(list) - 1)] + [1]
#     def generate(self, numRows: int):
#         result = []
#         for i in range(numRows):
#           tmp = self.generateList(result)
#           result = tmp
#         return result

class Solution:
    def generateList(self, list: list):
      return [1] + [list[i] + list[i + 1] for i in range(len(list) - 1)] + [1]
    def getRow(self, numRows: int):
        result = []
        if (not numRows):
          return [1]
        for i in range(numRows):
          tmp = self.generateList(result)
          result = tmp
        return result

x = Solution()
print(x.getRow(0))
