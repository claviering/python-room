# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def genTreeForList(self, rangeList):
      nodeList = []
      if len(rangeList) < 1:
        return [None]
      for index, value in enumerate(rangeList):
        nodeLeftList = self.genTreeForList(rangeList[:index])
        nodeRightList = self.genTreeForList(rangeList[index + 1:])
        for left in nodeLeftList:
          for right in nodeRightList:
            head = TreeNode(value)
            head.left = left
            head.right = right
            nodeList.append(head)
      return nodeList
    def generateTrees(self, n: int):
        if n < 1:
          return None
        rangeList = [i for i in range(1, n + 1)]
        res = self.genTreeForList(rangeList)
        return res

test = Solution()
print(test.generateTrees(3))