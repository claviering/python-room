# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    numTreesSet = {}
    def genTreeForList(self, rangeList):
      if len(rangeList) < 1:
        return 1
      key = "-".join([str(elem) for elem in rangeList])
      if key in self.numTreesSet:
        return self.numTreesSet[key]
      total = 0
      for index, value in enumerate(rangeList):
        nodeLeftList = self.genTreeForList(rangeList[:index])
        nodeRightList = self.genTreeForList(rangeList[index + 1:])
        total += nodeLeftList * nodeRightList
      self.numTreesSet[key] = total
      return total
    def numTrees(self, n: int):
        if n < 1:
          return 0
        rangeList = [i for i in range(1, n + 1)]
        return self.genTreeForList(rangeList)

test = Solution()
print(test.numTrees(12))
print(test.numTreesSet)