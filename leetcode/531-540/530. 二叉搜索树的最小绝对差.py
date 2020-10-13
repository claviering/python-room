# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def getMinimumDifference(self, root):
    nodeList = []
    self.dfs(root, nodeList)
    absList = [abs(nodeList[index] - nodeList[index + 1]) for index in range(len(nodeList) - 1)]
    return min(absList)
  # 中序遍历二叉树，返回数组
  def dfs(self, root, nodeList):
    if not root:
      return
    self.dfs(root.left, nodeList)
    nodeList.append(root.val)
    self.dfs(root.right, nodeList)